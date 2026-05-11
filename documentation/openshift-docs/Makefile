SHELL := /bin/bash
DISTRO ?= openshift-enterprise
WORKERS ?= 4
SOURCE_DIR := openshift-docs
DOCS_DIR := docs

.PHONY: docs clean clean-source

docs:
ifndef VERSION
	$(error VERSION is required. Usage: make docs VERSION=4.22)
endif
	@$(MAKE) $(DOCS_DIR)/$(VERSION)/AGENTS.md VERSION=$(VERSION)

$(DOCS_DIR)/%/AGENTS.md: convert.py | $(SOURCE_DIR)
	cd $(SOURCE_DIR) && git fetch --depth 1 origin enterprise-$* && git checkout FETCH_HEAD
	python3 convert.py \
		--source-dir $(SOURCE_DIR) \
		--output-dir $(DOCS_DIR)/$* \
		--distro $(DISTRO) \
		--branch enterprise-$* \
		--workers $(WORKERS)
	@echo "Docs generated at $(DOCS_DIR)/$*/"

$(SOURCE_DIR):
	git clone --depth 1 https://github.com/openshift/openshift-docs.git $(SOURCE_DIR)

clean-source:
	rm -rf $(SOURCE_DIR)

clean:
	rm -rf $(SOURCE_DIR) $(DOCS_DIR)
