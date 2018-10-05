.PHONY: all build test dist pypi-upload

all: build

build:
	pip install -r requirements.txt

test:
	python -m unittest discover

lint:
	pylint ridi

dist:
	rm -rf ./dist
	python setup.py sdist

pypi-upload:
	twine upload dist/*

release: dist pypi-upload