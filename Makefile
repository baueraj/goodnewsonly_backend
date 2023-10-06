.PHONY: test

test:
	pytest tests/

check:
	black .
	isort .
	flake8
	mypy .
	deptry .
