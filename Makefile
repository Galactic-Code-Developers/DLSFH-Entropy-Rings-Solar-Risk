.PHONY: setup lab

setup:
	python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt && python -m ipykernel install --user --name dlsfh-entropy-rings

lab:
	. .venv/bin/activate && jupyter lab
