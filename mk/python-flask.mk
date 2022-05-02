PACKAGE := template-python-flask
.PHONY: run
run: requirements  ## Run the application locally
	source .venv/bin/activate \
	&& flask run

# LINT_OPTS ?= --all
.PHONY: lint
lint: requirements-dev
	source .venv/bin/activate && pre-commit run $(LINT_OPTS)

.PHONY: test
test: test-unit  ## Launch tests for the application

# https://docs.pytest.org/en/7.1.x/how-to/usage.html
.PHONY: test-unit
test-unit: requirements-dev
	source .venv/bin/activate && python3 -m pytest tests/