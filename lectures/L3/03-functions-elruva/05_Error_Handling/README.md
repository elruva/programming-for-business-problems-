# 05 - Error Handling

Learn how to handle errors gracefully using try/except blocks.

## Exercises

| File | Type | Description |
|------|------|-------------|
| `01_predict.py` | Predict | Basic try/except for division by zero |
| `02_predict.py` | Predict | Handling multiple error types |
| `03_investigate.py` | Investigate | Build robust input validation |
| `04_modify.py` | Modify | Add try/except to a fragile temperature converter |

## Key Concepts

- **Exception** - an error that occurs during program execution
- **`try`** - code that might cause an error goes here
- **`except`** - code to run if an error occurs
- **`except ErrorType`** - catch a specific type of error
- **`finally`** - code that always runs (optional)

## Common Error Types

- **`ValueError`** - wrong type of value (e.g., `int("abc")`)
- **`ZeroDivisionError`** - dividing by zero
- **`TypeError`** - wrong type for an operation
- **`IndexError`** - list index out of range
- **`KeyError`** - dictionary key not found

## Help! My Code Doesn't Work!

Make sure that you check for the following things:
- `try` and `except` blocks must be paired
- Code inside `try` stops at the first error and jumps to `except`
- Catch specific errors when possible (not just bare `except:`)
- Put only the code that might fail inside `try`
- `except` blocks are indented at the same level as `try`
