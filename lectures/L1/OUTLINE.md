# L1 — Computational Thinking with Python

Instructor: Nikolai Stein (Aarhus University)

Course shape: broad, beginner-friendly (breadth over depth).
- Week 1 — Python fundamentals
- Week 2 — Computational thinking, web scraping
- Week 3 — Data analysis and simulation

---

## Session 0 — Introduction (19 slides)

### 1. About
- Instructor background: Senior Researcher (JMU Würzburg), Product Manager (SOLISTIQ), Visiting Professor (Aarhus), Lecturer (Mannheim / Gutenberg). BSc Business Management → MSc Information Systems → PhD Business Analytics.
- Course assumes little or no programming experience.
- Icebreaker: background, prior programming experience, field of study.

### 2. Fundamentals
- **Programming = getting computers to solve problems.** Two ideas: *you* (the computer only does what you tell it) and *solve problems* (computers are tools, not magic).
- **The computing cycle:** Input → Process → Output, with Storage alongside (saving data not currently in use).
- **Algorithm ≠ program.** An algorithm is a sequence of instructions describing the *logic*; a program is its *implementation* in a specific language. One algorithm → many languages.
- Everyday algorithms: making tea, Tic-Tac-Toe strategy, making a sandwich.
- Same algorithm, three languages:
  - Pseudocode: `OUTPUT "Hello, World"`
  - Python: `print("Hello, World!")`
  - JavaScript: `console.log("Hello, World!");`
  - Java: `System.out.println("Hello, World!");`

### 3. PRIMM framework
The teaching model used all course long:
| Stage | What you do |
|---|---|
| **P**redict | Look at working code — what will it do? |
| **R**un | Execute it and check your prediction |
| **I**nvestigate | What does each line mean? Trace it. |
| **M**odify | Edit the program to do something different |
| **M**ake | Design a new program with the same concepts |

Why it works: starting from working code instead of a blank screen lowers cognitive load and builds confidence; ownership of the code increases as you move Predict → Make.

### 4. Getting started
- Hands-on class run through **GitHub Codespaces** — browser IDE, no local install.
- Setup: create a GitHub account → open the course repo (link on Brightspace) → open the first exercise in Codespaces → start Session 1.

---

## Session 1 — Python Basics (29 slides)

**Learning goals:** comprehend, trace, adapt and create Python code that outputs text, assigns variables, reads input, refers to variables in later statements, and does simple arithmetic.

Structure mirrors Input → Process → Output.

### 1. Output
- `print()` displays text on screen; works with strings, numbers, variables.
  ```python
  print("Hello, World!")  # text
  print(42)               # integer
  print(3.14)             # decimal
  ```
- Python is **case-sensitive** and punctuation-strict: lowercase `print`, parentheses required, text must be quoted (`"..."` or `'...'`).
- Common errors: `Print("Hello")` (capital P), `print("Hello)` (missing quote).
- **Practice:** `01_Output` — `01_predict.py`, `02_predict.py`, `03_investigate.py`, `04_investigate.py`, `05_investigate.py`, `06_modify.py`, `07_make.py`.

### 2. Variables
- A variable is a labeled container storing a value — name on the left, value on the right of `=`.
  ```python
  counter = 100      # int
  miles   = 1000.0   # float
  name    = "John"   # str
  ```
- **Data types:** `int` (10, -5, 1000), `float` (3.14, -0.5, 99.99), `str` ("Hello", 'World'). The type determines which operations are legal.
- **f-strings** embed variables in text — prefix `f`, wrap variables in `{}`:
  ```python
  name = "Homer Simpson"; age = 39
  print(f"Hi! My name is {name}")
  print(f"I am {age} years old.")
  ```
- **String slicing:** `string[start:end]` gives characters from `start` up to `end-1`; indexing starts at 0, negative indices count from the end.
  ```python
  text = "Hello, World!"
  print(text[0:5])  # Hello
  print(text[-1])   # !
  ```
- **Practice:** `02_Variables` — `01_predict.py` … `05_modify.py`.

### 3. Input
- `input()` pauses the program, waits for the user, and returns what they typed.
- **Always returns a string** — this matters for the Math section.
  ```python
  name = input("What is your name? ")
  print(f"Hello, {name}!")
  ```
- **Practice:** `03_Input` — `01_predict.py` … `05_modify.py`.

### 4. Math (the "Process" step)
- Arithmetic operators:

  | Operator | Name | Example |
  |---|---|---|
  | `+` | Addition | `x + y` |
  | `-` | Subtraction | `x - y` |
  | `*` | Multiplication | `x * y` |
  | `/` | Division | `x / y` |
  | `%` | Modulus (remainder) | `x % y` |
  | `**` | Exponentiation | `x ** y` |
  | `//` | Floor division | `x // y` |

- Workflow: assign numbers → calculate → store result → output.
  ```python
  num1 = 5; num2 = 10
  result = num1 + num2
  print(result)   # 15
  ```
- **Shorthand operators:** `x += 5`, `x -= 5`, `x *= 5`, `x /= 5`.
- **Type conversion trap:** `input()` gives a string, so `"5" + "3"` → `"53"`. Wrap it:
  ```python
  num   = int(input("Number: "))
  price = float(input("Price: "))
  ```
  `int()` for whole numbers, `float()` for decimals.
- **Practice:** `04_Math` — `01_predict.py` … `05_modify.py`, then `05_Modify_Make` — `01_modify.py`, `02_modify.py`, `03_make.py`, `04_make.py`.

### Session takeaways
- Output with `print()`
- Variables store data; types `int` / `float` / `str`; format with f-strings
- `input()` reads from the user and always returns a string
- Math with `+ - * / // % **`; convert with `int()` / `float()` before calculating
