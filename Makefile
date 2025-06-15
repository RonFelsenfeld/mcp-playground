VENV := .venv
ACTIVATE := . $(VENV)/bin/activate

.PHONY: all setup activate install sync run-file run-server clean

all: setup

setup:
	uv venv $(VENV)

activate:
	@echo "Run this in your terminal to activate the virtual environment:"
	@echo "source $(VENV)/bin/activate"

sync:
	$(ACTIVATE) && uv sync

freeze-dependencies:
	$(ACTIVATE) && uv pip freeze > requirements.txt

run-file:
	$(ACTIVATE) && uv run python $(if $(file),$(file),src/main.py)

run-server:
	$(ACTIVATE) && uvicorn src.main:app --reload

clean:
	rm -rf $(VENV) uv.lock