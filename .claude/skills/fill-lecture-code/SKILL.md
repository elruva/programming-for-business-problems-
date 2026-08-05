---
name: fill-lecture-code
description: Fill in the course exercise .py files (predict / investigate / modify / make) with short answers and code. Use when the user asks to complete, answer, or fill out lecture or assignment Python exercises.
---

# Filling out lecture exercise code

Course exercises are `.py` files with blank comment slots. Fill them in, keeping
everything at the level of a first-week beginner.

## Rules

0. **Read the sources first.** Use the `lecture-sources` skill to read the
   lecture's `OUTLINE.md`, folder `README.md` files, any session `.py` code, and
   the slide PDF. Answers should reuse what the lecture actually showed.
1. **Stay inside the syllabus.** Check today's date against the lecture schedule
   in `CLAUDE.md` and use only constructs already taught. Before lecture 2: no
   `if`, no loops. Before 3: no `def`. Before 4: no lists or dicts. Never
   comprehensions or `lambda` unless the user asks.
2. **One short sentence per answer.** Plain words. No jargon the lectures have
   not used. Write it as the student would, not as a textbook would.
3. **Run the file before answering.** Never guess an error message or an output —
   quote what Python actually printed.
4. **Answers go in the file**, on the line after each `# Answer:` or `# Fix:`.
   Don't restructure or reformat the rest of the file.
5. **When the exercise asks for code, write real code — never commented-out
   code.** This is the important one. Explanations are comments; solutions are
   not. If the task says "write a print statement", "modify the line above",
   "use slicing to print the year" or similar, the answer must be a live line
   that runs when the file is executed.

   ```python
   # 2. Write a print statement that outputs your favorite number:
   print(17)          # correct - real code
   # print(17)        # wrong - does nothing when the file runs
   ```

   The one exception is a `# Fix:` line inside an `_investigate.py` file, which
   is a written answer. Fix the actual broken code above it as well.
6. **Verify at the end** by running every file you touched**, and check the
   output is what the exercise asked for** — not just that it runs without an
   error.

## The four file types

| File | What to do |
|---|---|
| `NN_predict.py` | Fill `# MY PREDICTION:` with the exact expected output, then answer the `# Q:` lines. |
| `NN_investigate.py` | Run it, paste the real error, say what is wrong in one sentence, then write the corrected line after `# Fix:`. Fix the broken code itself too. |
| `NN_modify.py` | Add the smallest code that meets each numbered task. Leave personal details (name, favourite number) as obvious placeholders. |
| `NN_make.py` | Write the program from scratch using the simplest approach. |

Some shipped `investigate` files have no actual bug (e.g. `01_Output/04` and
`05`). Answer for the bug described in the folder `README.md`, and tell the user
the file was already correct.

## When there is more than one way

The **chosen answer is always live code** (rule 5). Only the *alternatives* are
commented out — a file cannot run four versions of the same task without printing
its output four times. Keep the simplest solution active and put the rest below:

```python
# Write your code below:
print("Line one")
print("Line two")


# ============================================================
# OTHER WAYS TO WRITE THE SAME THING
# Uncomment one at a time (remove the #) and run it.
# ============================================================

# Option A - one print with \n. \n means "new line".
# print("Line one\nLine two")

# Option B - triple quotes. The string can span real lines.
# print("""Line one
# Line two""")
```

Guidelines for the options block:

- Two to four options is plenty.
- One line of explanation each — what it demonstrates, or when you would use it.
- Order them simplest first.
- Mention a gotcha where one exists (e.g. leading spaces inside triple quotes get
  printed).
- **Every *alternative* must be commented out** — the chosen solution above them
  stays live. If the alternatives run too, the file prints its output several
  times over. Run the file afterwards and confirm the output appears once.
- Tell the user that uncommenting an option means commenting out the active one,
  or the output repeats.
- If an option uses something not yet taught, say so in its comment.

## After finishing

Tell the user, briefly:
- which files were changed and what went into each,
- anything that needs their own input (their name, their number),
- anything odd found along the way (a file with no bug, a README that disagrees
  with the code).
