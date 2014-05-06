release:
	python setup.py sdist bdist_wheel upload -r pypi

# Test it via `pip install -i https://testpypi.python.org/pypi murl`
test-release:
	python setup.py sdist bdist_wheel upload -r test

clean:
	rm -rf dist/
	rm MANIFEST
	find . -name "*.pyc" -exec rm {} \;
