#!/usr/bin/env python3
"""
Convert Hugo-rendered Kubernetes documentation HTML to GitHub-Flavored Markdown.

Usage:
    python convert.py --source-dir ./kubernetes-website/public --output-dir ./docs/1.34
"""

import argparse
import os
import re
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify as md


def extract_lang(el):
    """Extract code language from a <pre> or <code> element's class."""
    classes = el.get("class", [])
    if isinstance(classes, str):
        classes = [classes]
    for cls in classes:
        if cls.startswith("language-"):
            return cls.replace("language-", "")
    return ""


def convert_file(source_file: str, dest_file: str) -> tuple[bool, str, str]:
    """Convert a single HTML file to Markdown."""
    source_path = Path(source_file)
    dest_path = Path(dest_file)

    if not source_path.exists():
        return False, str(source_path), "Source file not found"

    try:
        html = source_path.read_text(encoding="utf-8", errors="replace")
        soup = BeautifulSoup(html, "html.parser")

        content = soup.find("div", class_="td-content")
        if not content:
            return False, str(source_path), "No td-content div found"

        for meta in content.find_all("header", class_="article-meta"):
            meta.decompose()
        for comment in content.find_all(string=lambda t: isinstance(t, type(soup.new_string(""))) is False and hasattr(t, 'strip') is False):
            pass

        for comment in content.find_all(string=lambda text: isinstance(text, str) and text.strip().startswith("<!--")):
            pass

        import bs4
        for comment in content.find_all(string=lambda text: isinstance(text, bs4.Comment)):
            comment.extract()

        for alert in content.find_all("div", class_="alert"):
            heading = alert.find(class_="alert-heading")
            label = heading.get_text(strip=True) if heading else "Note:"
            if heading:
                heading.decompose()
            inner_html = alert.decode_contents()
            inner_md = md(
                inner_html,
                heading_style="ATX",
                code_language_callback=extract_lang,
                escape_asterisks=False,
                escape_underscores=False,
            ).strip()
            blockquote_lines = [f"> **{label}**"]
            for line in inner_md.splitlines():
                blockquote_lines.append(f"> {line}" if line.strip() else ">")
            new_tag = soup.new_tag("div")
            new_tag.string = "\n".join(blockquote_lines)
            alert.replace_with(new_tag)

        result = md(
            str(content),
            heading_style="ATX",
            code_language_callback=extract_lang,
            strip=["script", "style"],
            escape_asterisks=False,
            escape_underscores=False,
        )

        result = post_process_markdown(result)

        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dest_path.write_text(result, encoding="utf-8")

        return True, str(source_path), "OK"

    except Exception as e:
        return False, str(source_path), str(e)


def post_process_markdown(content: str) -> str:
    """Clean up markdownify output artifacts."""
    content = re.sub(r"\n{3,}", "\n\n", content)

    lines = content.splitlines()
    cleaned = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("<!--") and stripped.endswith("-->"):
            continue
        cleaned.append(line.rstrip())
    content = "\n".join(cleaned)

    content = re.sub(r"\n{3,}", "\n\n", content)

    return content.strip() + "\n"


def collect_html_files(source_dir: str) -> list[dict]:
    """Walk the public/docs/ directory and collect all HTML files."""
    docs_path = Path(source_dir) / "docs"
    if not docs_path.exists():
        print(f"Error: {docs_path} does not exist")
        sys.exit(1)

    files = []
    for html_file in docs_path.rglob("index.html"):
        rel_path = html_file.parent.relative_to(docs_path)
        if str(rel_path).startswith("_print"):
            continue
        if str(rel_path) == ".":
            continue

        files.append({
            "source": str(html_file),
            "rel_path": str(rel_path),
        })

    return files


def generate_agents_md(output_dir: str) -> None:
    """Generate a compressed pipe-delimited AGENTS.md index."""
    output_path = Path(output_dir)
    lines = [
        "# Kubernetes Documentation Index",
        "",
        "> IMPORTANT: Prefer retrieval-led reasoning over pre-training-led",
        "> reasoning for Kubernetes tasks. Read the referenced files rather",
        "> than relying on training data which may be outdated.",
        "",
        "## How to Use This Index",
        "",
        "This is a compressed documentation map. Each entry lists topic",
        "files using pipe-delimited format: `|section/subsection:{file1.md,file2.md}`.",
        "Retrieve the specific file you need rather than reading everything.",
        "",
        f"Root: ./",
        "",
        "## Documentation Map",
        "",
    ]

    dir_files: dict[str, list[str]] = {}
    for md_file in sorted(output_path.rglob("*.md")):
        if md_file.name == "AGENTS.md":
            continue
        rel = md_file.relative_to(output_path)
        parent = str(rel.parent)
        if parent == ".":
            continue
        dir_files.setdefault(parent, []).append(rel.name)

    current_section = None
    for dir_path in sorted(dir_files.keys()):
        section = dir_path.split("/")[0]
        if section != current_section:
            current_section = section
            lines.append(f"### {section}")
            lines.append("")

        files_str = ",".join(dir_files[dir_path])
        lines.append(f"|{dir_path}:{{{files_str}}}")

    lines.append("")
    (output_path / "AGENTS.md").write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Convert Hugo-rendered Kubernetes docs HTML to Markdown"
    )
    parser.add_argument(
        "--source-dir",
        required=True,
        help="Path to Hugo public/ output directory",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Output directory for Markdown files",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Number of parallel workers (default: 4)",
    )
    args = parser.parse_args()

    source_dir = os.path.abspath(args.source_dir)
    output_dir = os.path.abspath(args.output_dir)

    print("Collecting HTML files...")
    html_files = collect_html_files(source_dir)
    print(f"Found {len(html_files)} pages to convert")

    os.makedirs(output_dir, exist_ok=True)

    successes = 0
    failures = 0

    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        futures = {}
        for entry in html_files:
            dest = os.path.join(output_dir, entry["rel_path"] + ".md")
            future = executor.submit(convert_file, entry["source"], dest)
            futures[future] = entry

        for future in as_completed(futures):
            entry = futures[future]
            success, path, message = future.result()
            if success:
                successes += 1
            else:
                failures += 1
                print(f"  FAIL: {entry['rel_path']} — {message}")

    print(f"\nConversion complete: {successes} succeeded, {failures} failed")

    print("Generating AGENTS.md index...")
    generate_agents_md(output_dir)

    print(f"Output written to {output_dir}/")


if __name__ == "__main__":
    main()
