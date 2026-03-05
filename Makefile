VENV=.venv
PYTHON?=python3.12
PY=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

setup:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install -U pip setuptools wheel
	$(PIP) install -r requirements.txt

ingest:
	$(PY) ingest.py

run:
	$(VENV)/bin/streamlit run app.py

clean:
	rm -rf vector_db docs.npy vector.index