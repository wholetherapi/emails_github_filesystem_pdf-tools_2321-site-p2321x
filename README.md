# Patrick Lee - Research Portfolio

Source for my personal research portfolio (Jekyll). The publication data lives in
`_data/registry.json`; each record renders as one card on the home page.

## Editing records

Run the validator after editing the data file:

```bash
python scripts/validate_registry.py _data/registry.json
```

The site generator expects a fixed record shape. Adding or renaming keys will fail
the build, so keep every record on the schema already used in the file.
