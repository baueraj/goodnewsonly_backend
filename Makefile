.PHONY: test

test:
	pytest -s tests/

check:
	black .
	isort .
	flake8
	mypy .
	deptry .
