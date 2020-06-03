help:
	@echo "venv      - Create vispp_venv and install all necessary dependencies."
	@echo "test      - Run tests. Requires virtual env set up."

venv:
	rm -rf vispp_venv ;\
	python3 -m venv vispp_venv ;\
	. vispp_venv/bin/activate ;\
	pip install -r requirements.txt ;\
	pip install -e .

test:
	. vispp_venv/bin/activate ;\
	python -m pytest tests/
