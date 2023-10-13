SHELL := /bin/bash

root := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
venv := $(root)/.venv
requirements := $(root)/requirements.txt

dirs := $(root)/lib

pylint := $(venv)/bin/pylint
pycodestyle := $(venv)/bin/pycodestyle
pycoverage := $(venv)/bin/coverage

venv: $(venv)/timestamp
$(venv)/timestamp: $(requirements)
	echo "Creating venv"
	test -d $(venv) || python3 -m venv $(venv)
	source $(venv)/bin/activate; python -m pip install --upgrade pip; python3 -m pip install -r $(requirements)
	touch $(venv)/timestamp


pylint: venv
	$(pylint) $(dirs)

pycodestyle: venv
	$(pycodestyle) $(dirs) --ignore=E501  # Ignore too long line

pycoverage: venv
	$(pycoverage) run -m pytest
	$(pycoverage) report -m --omit=*/tests/*,__init__.py --skip-empty --skip-covered | tee $(root)/.coverage_report.txt
	@grep -E "TOTAL\s+181\s+58\s+68%" $(root)/.coverage_report.txt

static: pylint pycodestyle
dynamic: pycoverage

test: static