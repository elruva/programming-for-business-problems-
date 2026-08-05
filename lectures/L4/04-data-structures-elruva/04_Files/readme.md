# 04 - Files

Learn how to read from and write to files in Python.

## Exercises

| File | Type | Description |
|------|------|-------------|
| `01_predict.py` | Predict | Read file line by line with `with` statement |
| `02_predict.py` | Predict | Read entire file content at once |
| `03_predict.py` | Predict | Write text to a file |
| `04_predict.py` | Predict | Append to an existing file |
| `05_predict.py` | Predict | Read and process CSV-like data |
| `06_investigate.py` | Investigate | Count lines and words in a file |
| `07_investigate.py` | Investigate | Filter and transform file data |
| `08_investigate.py` | Investigate | Work with structured data files |
| `09_modify.py` | Modify | Read a CSV inventory and write a summary report |
| `10_make.py` | Make | Build a word-frequency counter that reads and writes files |

## Key Concepts

- **`open(filename, mode)`** - open a file for reading or writing
- **`"r"`** - read mode (default)
- **`"w"`** - write mode (overwrites existing file)
- **`"a"`** - append mode (adds to end of file)
- **`with` statement** - automatically closes file when done
- **`file.read()`** - read entire file as string
- **`file.readlines()`** - read file as list of lines

## Help! My Code Doesn't Work!

Make sure that you check for the following things:
- File paths must be correct (check the folder name)
- Use `"r"` for reading, `"w"` for writing, `"a"` for appending
- Remember to close files or use `with` statement
- When writing, add `"\n"` for new lines
- `"w"` mode erases existing content - use `"a"` to preserve it
