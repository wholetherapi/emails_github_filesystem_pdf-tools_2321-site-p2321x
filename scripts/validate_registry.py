#!/usr/bin/env python3
"""Validate _data/registry.json for the portfolio site."""
import json
import sys

ITEM_KEYS = {
    "slug", "title", "authors", "venue", "year",
    "status", "source_url", "summary",
}
STATUSES = {"published", "accepted", "under_review"}
GITHUB_PREFIX = "https://github.com/"


def fail(message):
    print("registry invalid: " + message)
    sys.exit(1)


def main(path):
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        fail("top-level value must be a JSON array")
    seen = set()
    for index, item in enumerate(data):
        if not isinstance(item, dict):
            fail("record %d is not an object" % index)
        if set(item.keys()) != ITEM_KEYS:
            fail("record %d has keys %s, expected %s" % (
                index, sorted(item.keys()), sorted(ITEM_KEYS)))
        if item["slug"] in seen:
            fail("duplicate slug %r" % item["slug"])
        seen.add(item["slug"])
        if not isinstance(item["authors"], list) or not item["authors"]:
            fail("record %d: authors must be a non-empty list" % index)
        if not isinstance(item["year"], int):
            fail("record %d: year must be an integer" % index)
        if item["status"] not in STATUSES:
            fail("record %d: unsupported status %r" % (index, item["status"]))
        url = item["source_url"]
        if not isinstance(url, str):
            fail("record %d: source_url must be a string" % index)
        if url and not url.startswith(GITHUB_PREFIX):
            fail("record %d: source_url must be empty or a github URL" % index)
    print("registry OK: %d records" % len(data))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "_data/registry.json")
