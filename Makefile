release:
	python setup.py sdist upload

pyc:
	find . -name "*.pyc" -exec rm {} \;
