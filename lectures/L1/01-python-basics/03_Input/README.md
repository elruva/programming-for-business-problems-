# 03 - Input

Learn how to get data from users using the `input()` function.

## Exercises

| File | Type | Description |
|------|------|-------------|
| `01_predict.py` | Predict | Basic input() without a prompt |
| `02_predict.py` | Predict | Input with text prompts |
| `03_investigate.py` | Investigate | Debug a NameError caused by forgetting to store input() |
| `04_investigate.py` | Investigate | Combine input() with string slicing to build initials |
| `05_modify.py` | Modify | Add prompts for city and favorite color, then print a sentence |

## Key Concepts

- **`input()`** - pauses program and waits for user to type something
- **Prompts** - text inside input() shows a message: `input("Enter name: ")`
- **Storage** - always assign input() to a variable or the data is lost
- **Data type** - input() ALWAYS returns a string, even if user types a number

## Help! My Code Doesn't Work!

Make sure that you check for the following things:
- Store the result of input() in a variable: `name = input("Name: ")`
- If you need a number, convert it: `age = int(input("Age: "))`
- Add a space after your prompt text for readability: `"Name: "`
