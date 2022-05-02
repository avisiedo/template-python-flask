.venv:
	python3 -m venv .venv
	source .venv/bin/activate && pip install --upgrade pip
	source .venv/bin/activate && pip install -r $(REQUIREMENTS)

.PHONY: requirements
requirements: REQUIREMENTS=requirements.txt
requirements: .venv

.PHONY: requirements-dev
requirements-dev: REQUIREMENTS=requirements-dev.txt
requirements-dev: .venv
