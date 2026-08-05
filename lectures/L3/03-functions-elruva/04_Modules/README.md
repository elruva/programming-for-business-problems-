# 04 - Modules

Learn how to use Python's built-in modules and import external functionality.

## Exercises

| File | Type | Description |
|------|------|-------------|
| `01_predict.py` | Predict | Using the `random` module for a dice game |
| `02_predict.py` | Predict | Using `math` and other standard modules |
| `03_investigate.py` | Investigate | Explore different import styles |
| `04_modify.py` | Modify | Expand the number guessing game with new features |

## Key Concepts

- **Module** - a file containing Python code (functions, variables, classes)
- **`import`** - brings a module into your program
- **`import module`** - access with `module.function()`
- **`from module import function`** - access directly as `function()`
- **Standard library** - Python's built-in collection of modules

## Common Modules

- **`random`** - generate random numbers (`randint`, `choice`, `shuffle`)
- **`math`** - mathematical functions (`sqrt`, `floor`, `ceil`, `pi`)
- **`datetime`** - work with dates and times

## Help! My Code Doesn't Work!

Make sure that you check for the following things:
- Module is imported before it's used
- Use correct syntax: `module.function()` or `function()` depending on import style
- Check spelling of module and function names (case-sensitive)
- Some modules need to be installed separately (not in standard library)
