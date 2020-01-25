all: sdist upload

sdist:
	python3 setup.py sdist

upload:
	twine upload dist/*

test:
	python3 -m pytest --cov=cryptocompare

.PHONY: sdist upload test
