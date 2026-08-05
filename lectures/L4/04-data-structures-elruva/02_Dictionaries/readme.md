# 02 - Dictionaries

Learn how to store data as key-value pairs.

## Exercises

| File | Type | Description |
|------|------|-------------|
| `01_predict.py` | Predict | Create dictionaries and count occurrences |
| `02_predict.py` | Predict | Access and modify dictionary values |
| `03_predict.py` | Predict | Loop through dictionaries |
| `04_investigate.py` | Investigate | Analyze dictionary operations |
| `05_investigate.py` | Investigate | Work with nested dictionaries |
| `06_modify.py` | Modify | Aggregate quarterly sales across employees |
| `07_make.py` | Make | Build a phone-book application with nested dicts |

## Key Concepts

- **Dictionary** - collection of key-value pairs in curly braces `{}`
- **Key** - unique identifier to access a value
- **Value** - data stored under a key
- **`dict[key]`** - access value by key
- **`dict.get(key, default)`** - access with fallback value
- **`dict.keys()`, `.values()`, `.items()`** - iterate over parts

## Help! My Code Doesn't Work!

Make sure that you check for the following things:
- The dictionary name is identical everywhere it is used (capitals matter)
- Dictionaries are indexed using keys, not numeric indices
- String keys must be in quotation marks
- Use `dict.get(key, default)` to avoid `KeyError` for missing keys
- Keys must be unique - adding a duplicate key overwrites the value
