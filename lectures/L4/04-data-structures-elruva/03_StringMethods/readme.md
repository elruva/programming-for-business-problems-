# 03 - String Methods

Learn how to clean and transform text data using string methods.

## Exercises

| File | Type | Description |
|------|------|-------------|
| `01_predict.py` | Predict | Whitespace removal with `strip()`, `lstrip()`, `rstrip()` |
| `02_predict.py` | Predict | Case conversion with `upper()`, `lower()`, `title()` |
| `03_predict.py` | Predict | Splitting strings with `split()` |
| `04_predict.py` | Predict | Joining lists with `join()` |
| `05_investigate.py` | Investigate | Combine string methods for data cleaning |
| `06_investigate.py` | Investigate | Search and replace with `find()` and `replace()` |
| `07_modify.py` | Modify | Clean and normalize messy product data |
| `08_make.py` | Make | Build an email-validator with deduplication |
| `09_make.py` | Make | Parse CSV lines into a list of dicts and summarize |

## Key Concepts

- **`strip()`** - remove whitespace from both ends
- **`split(separator)`** - split string into a list
- **`join(list)`** - combine list items into a string
- **`upper()`, `lower()`** - change case
- **`replace(old, new)`** - replace substrings
- **`find(substring)`** - find position of substring (-1 if not found)

## Help! My Code Doesn't Work!

Make sure that you check for the following things:
- String methods return **new strings** - they don't modify the original
- Method names are lowercase (e.g., `strip()` not `Strip()`)
- The separator for `split()` and `join()` must be a string
- `join()` is called on the separator: `", ".join(list)`
- Remember to store the result: `text = text.strip()`
