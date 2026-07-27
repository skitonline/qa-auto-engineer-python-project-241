install:
	uv sync

update:
	uv lock --upgrade
	uv sync

test:
	uv run pytest

lint:
	uv run ruff check

check: test lint

build:
	uv build

package-install: build
	uv tool install --force $(wildcard dist/*.whl)

.PHONY: install update test lint selfcheck check build