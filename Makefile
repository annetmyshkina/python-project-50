install:
	uv sync

build:
	uv build

run:
	uv run gendiff data/file1.json data/file2.json


reinstall:
	uv tool install --force dist/hexlet_code-0.1.0-py3-none-any.whl

check:
	uv run ruff check gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml