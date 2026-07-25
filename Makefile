install:
	uv lock --upgrade
	uv sync

build:
	uv build

lint:
	uv run ruff check

package-install: build
	uv tool install --force $(wildcard dist/*.whl)