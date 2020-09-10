.PHONY: clean install all default
.DEFAULT_GOAL = default

default: install clean format lint coverage

clean:
	@echo "remove all build, test, coverage and Python artifacts"
	rm -fr build dist .eggs *egg-info .tox/ .cache/ .pytest_cache/ docs/_build/ .coverage htmlcov +
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.PHONY: install
install:
	poetry install

format:
	# Sort imports one per line, so autoflake can remove unused imports
	poetry run isort --recursive  --force-single-line-imports --apply app tests
	poetry run autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place app --exclude=__init__.py
	poetry run black app tests
	poetry run isort --recursive --apply app tests

lint:
#	poetry run mypy --show-error-codes app
	poetry run flake8

test: install
	poetry run pytest

coverage: install
	poetry run pytest --cov=app --cov-report=term-missing tests
