# 02 - Parameters

Learn how to pass data into functions using parameters and arguments.

## Exercises

| File | Type | Description |
|------|------|-------------|
| `01_predict.py` | Predict | Functions with single parameters |
| `02_predict.py` | Predict | Functions with multiple parameters and default values |
| `03_investigate.py` | Investigate | Analyze parameter passing and default values |
| `04_modify.py` | Modify | Add parameters and defaults to a shipping calculator |

## Key Concepts

- **Parameter** - variable in the function definition that receives data
- **Argument** - actual value passed when calling the function
- **Default parameter** - parameter with a preset value (e.g., `def greet(name="World")`)
- **Positional arguments** - matched by position in the function call
- **Keyword arguments** - matched by name (e.g., `greet(name="Alice")`)

## Help! My Code Doesn't Work!

Make sure that you check for the following things:
- Number of arguments matches number of required parameters
- Arguments are in the correct order (unless using keyword arguments)
- Parameters without default values must receive an argument
- Don't use mutable default values like lists (use `None` instead)
