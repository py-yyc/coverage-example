
test:
	flake8 ttt/*.py
	coverage run --source=ttt --branch -m pytest -v tests/test_*.py
	coverage report --show-missing
	cuv graph
