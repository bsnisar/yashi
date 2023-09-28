# Variables
PYTHON = python3
PACKAGE_NAME = my_cli
DIST_DIR = dist

# Targets
all: clean build

clean:
	@echo "Cleaning up..."
	rm -rf $(DIST_DIR) __pycache__

build:
	@echo "Building $(PACKAGE_NAME)..."
	$(PYTHON) setup.py sdist bdist_wheel

install:
	@echo "Installing $(PACKAGE_NAME) locally..."
	pip install .

uninstall:
	@echo "Uninstalling $(PACKAGE_NAME)..."
	pip uninstall -y $(PACKAGE_NAME)

publish:
	@echo "Publishing $(PACKAGE_NAME) to PyPI..."
	twine upload $(DIST_DIR)/*

.PHONY: all clean build install uninstall publish
