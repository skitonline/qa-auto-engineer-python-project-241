install:
	uv sync

update:
	uv lock --upgrade
	uv sync

run:
	uv run gendiff tests/test_data/input/file1.json tests/test_data/input/file2.json

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

lint:
	uv run ruff check

check: test lint

build:
	uv build

package-install: build
	uv tool install --force $(wildcard dist/*.whl)