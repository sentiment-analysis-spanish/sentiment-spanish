
# pip3 install --user --upgrade twine

# pip3 install --user --upgrade setuptools wheel

python3 setup.py sdist bdist_wheel

# twine upload --repository-url https://test.pypi.org/legacy/ dist/*

python3 -m twine upload dist/*