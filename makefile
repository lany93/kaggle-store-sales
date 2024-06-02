SHELL := /bin/bash
POETRY_VERSION='$(shell poetry --version)'
VENV = .venv

.DEFAULT_GOAL = help

help:
	@echo "---------------HELP-----------------"
	@echo "Set up project: make setup"
	@echo "Activate venv: make venv"
	@echo ""
	@echo ""
	@echo ""
	@echo ""
	@echo "------------------------------------"

check_poetry_version:
ifneq "1.8.2" "$(word 1, $(sort 1.8.2 $(POETRY_VERSION_SHORT)))"
	$(warning "Recommended: Update Poetry version to >= 1.8.2")
endif


install:
	@echo "************  Setup poetry ************"
	pip install poetry
	poetry config virtualenvs.in-project true
	poetry install

	@echo "************  Install pre-commit ************"
	pip install pre-commit
	pre-commit install


venv: 
	poetry shell

setup: install check_poetry_version