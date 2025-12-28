# Engine

## Testing

To run the tests using `uv` from within this directory (`engine`), use the following command:

```bash
uv run pytest world/tests/
```

This ensures that the `engine` module is correctly resolved from the parent directory by configuring `pythonpath` in `pyproject.toml`.
