# 04 - Math

Learn arithmetic operations and type conversion in Python.

## Exercises

| File | Type | Description |
|------|------|-------------|
| `01_predict.py` | Predict | Basic arithmetic operators (+, -, *, /, //, **, %) |
| `02_predict.py` | Predict | Math with variables and compound operators (+=, -=) |
| `03_investigate.py` | Investigate | Debug a TypeError when mixing int with input() |
| `04_investigate.py` | Investigate | String concatenation vs. number addition |
| `05_modify.py` | Modify | Fix and extend an average calculator |

## Key Concepts

- **Arithmetic operators** - `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Floor division** - `//` divides and rounds down to integer
- **Modulus** - `%` returns the remainder after division
- **Exponentiation** - `**` raises to a power (e.g., `2 ** 3` = 8)
- **Compound operators** - `+=`, `-=`, `*=`, `/=` update a variable
- **Type conversion** - `int()` and `float()` convert strings to numbers

## Help! My Code Doesn't Work!

Make sure that you check for the following things:
- `input()` always returns a string - use `int()` or `float()` to convert
- Division `/` always returns a float (e.g., `10/5` = `2.0`)
- Use `//` for integer division
- `"5" + "3"` is string concatenation ("53"), not math!
