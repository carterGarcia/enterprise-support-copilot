VENV=.venv
PYTHON?=python3.12
PY=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
STREAMLIT=$(VENV)/bin/streamlit

.PHONY: help setup ingest run clean

help:
	@echo "Targets:"
	@echo "  make setup            Create venv and install dependencies"
	@echo "  make ingest           Build local vector store in vector_db/"
	@echo "  make run              Start Streamlit app"
	@echo "  make clean            Remove generated artifacts"

setup:
	$(PYTHON) -m venv $(VENV)
	$(PY) -m pip install -U pip setuptools wheel
	$(PIP) install -r requirements.txt

ingest:
	$(PY) ingest.py

run:
	$(STREAMLIT) run app.py

clean:
	rm -rf vector_db docs.npy vector.index