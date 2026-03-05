VENV=.venv
PY=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

setup:
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

ingest:
	$(PY) ingest.py

run:
	$(VENV)/bin/streamlit run app.py

clean:
	rm -rf vector_db docs.npy vector.index