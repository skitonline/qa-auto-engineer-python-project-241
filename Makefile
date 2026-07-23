install:
	uv lock --upgrade
	uv sync

build:
	uv run ruff check --fix
	uv run ruff format
	uv build

lint:
	uv run ruff check

package-install: build
	uv tool install --force $(wildcard dist/*.whl)