
test:
	flake8 ttt/*.py
	coverage run --source=ttt --branch -m pytest -v tests/test_*.py
	coverage html
	coverage report --show-missing
	cuv graph
