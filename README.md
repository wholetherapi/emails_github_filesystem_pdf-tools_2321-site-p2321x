# Patrick Lee — Research Portfolio

Jekyll source for my research portfolio. Publication metadata lives in `_data/registry.json`; the homepage renders one card per item.

Records are validated before deploy:

```bash
python scripts/validate_registry.py _data/registry.json
```

The generator expects a stable record shape, so every item keeps the same fixed set of keys.
