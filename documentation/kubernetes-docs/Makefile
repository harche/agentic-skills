SHELL := /bin/bash
WORKERS ?= 4
SOURCE_DIR := kubernetes-website
DOCS_DIR := docs
HUGO ?= hugo

.PHONY: docs clean clean-source

docs:
ifndef VERSION
	$(error VERSION is required. Usage: make docs VERSION=1.34)
endif
	@$(MAKE) $(DOCS_DIR)/$(VERSION)/AGENTS.md VERSION=$(VERSION)

$(DOCS_DIR)/%/AGENTS.md: convert.py | $(SOURCE_DIR)
	cd $(SOURCE_DIR) && git fetch --depth 1 origin release-$* && git checkout FETCH_HEAD
	cd $(SOURCE_DIR) && npm install
	cd $(SOURCE_DIR) && $(HUGO) --cleanDestinationDir --environment development
	python3 convert.py \
		--source-dir $(SOURCE_DIR)/public \
		--output-dir $(DOCS_DIR)/$* \
		--workers $(WORKERS)
	@echo "Docs generated at $(DOCS_DIR)/$*/"

$(SOURCE_DIR):
	git clone --depth 1 https://github.com/kubernetes/website.git $(SOURCE_DIR)

clean-source:
	rm -rf $(SOURCE_DIR)

clean:
	rm -rf $(SOURCE_DIR) $(DOCS_DIR)
