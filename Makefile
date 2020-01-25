all: sdist

sdist:
	python3 setup.py sdist

upload:
	twine upload dist/*

mypy:
	python3 -m mypy cryptocompare/cryptocompare.py

test:
	python3 -m pytest --mypy --cov=cryptocompare tests/

.PHONY: sdist upload mypy test
