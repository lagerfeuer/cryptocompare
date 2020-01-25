all: sdist

sdist:
	python3 setup.py sdist

upload:
	twine upload dist/*

test:
	python3 -m pytest --mypy --cov=cryptocompare tests/

.PHONY: sdist upload test
