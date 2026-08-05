# Daily Practice Guide

20–30 minutes a day.

---

## 1. Go to today's folder, then run files

Two lines to start:

```bash
cd ~/computational/lectures/L2/02-flow-control-elruva/01_Boolean_Conditions
python 04_modify.py
```

`cd` once into the folder you're working in, then every file in it is just its
own name — no path. Stay there for the whole session.

Press `Tab` while typing to complete each folder name; keep hitting it after
each `/`. Then `↑` and Enter to re-run after an edit.

The folders:

```
~/computational/lectures/
├── L1/01-python-basics/       01_Output  02_Variables  03_Input  04_Math  05_Modify_Make
└── L2/02-flow-control-elruva/ 01_Boolean_Conditions  02_Selection  03_Iteration
```

Next day, swap the last part:

```bash
cd ~/computational/lectures/L2/02-flow-control-elruva/02_Selection
```

## 2. Two prompts, don't mix them up

| Prompt | Understands | Example |
|---|---|---|
| `❯` | shell commands | `cd 02_Selection`, `ls`, `python 01_predict.py` |
| `>>>` | Python | `year = 2024` |

Python typed at `❯` gives `command not found`. A shell command typed at `>>>`
gives a `SyntaxError`. `Ctrl+D` leaves `>>>`.

**Never paste a multi-line block into `>>>`.** The `input()` question repeats
itself dozens of times — that's the prompt being redrawn, not your code running
twice. Put the code in a file and run it instead.

## 3. If you'd rather not cd

Run from anywhere with the full path — same result, more typing:

```bash
python ~/computational/lectures/L2/02-flow-control-elruva/01_Boolean_Conditions/04_modify.py
```

`ls` lists the files in the folder you're in. Lost? `pwd` says where you are,
and `cd ~/computational/lectures` puts you back.

---

## 4. The PRIMM loop

Do the stages in order. Don't skip Predict — guessing first is what makes it stick.

1. **Predict** — before running, write what you think the output is in the `# MY PREDICTION:` comment.
2. **Run** — `python <file>`. Where you were wrong is the lesson.
3. **Investigate** — answer the `# Q1:` / `# Q2:` comments in your own words.
4. **Modify** — change it, re-run. Try to break it: remove a quote, capitalise `Print`. Read the error, fix it.
5. **Make** — write the program from blank, no copying.

Answers go **in the file as comments**.

File order in every folder: `predict` → `investigate` → `modify` → `make`.

---

## 5. When something breaks

Read the error's **last line first** — it names the problem.

| You see | Cause |
|---|---|
| `can't find '__main__' module` | You gave `python` a folder. It needs a `.py` file. |
| `No such file or directory` | Typo in the path. Use `Tab` to complete it. |
| `NameError: name 'Print' is not defined` | Capital letter — Python is case-sensitive. |
| `SyntaxError: unterminated string literal` | Missing quote. |
| `SyntaxError: '(' was never closed` | Missing `)`. |
| `TypeError: can only concatenate str` | Math on `input()` without `int()` / `float()`. |
| `IndentationError` | Stray spaces at the start of a line. |
| `>>>` instead of `❯` | You're inside Python. Press `Ctrl+D`. |
| The question prints 3–4 times | You pasted into `>>>`. `Ctrl+D`, then run the file. |
| Nothing happens | It's waiting for you. Type an answer, press Enter. |
| Stuck | `Ctrl+C` |

Always `python`, never `python3`.

---

## 6. Schedule

One folder a day.

| Day | Folder |
|---|---|
| 1 | `L1/.../01_Output` — 7 files |
| 2 | `L1/.../02_Variables` — 5 |
| 3 | `L1/.../03_Input` — 5 |
| 4 | `L1/.../04_Math` — 5 |
| 5 | `L1/.../05_Modify_Make` — 4 |
| 6 | `L2/.../01_Boolean_Conditions` — 5 |
| 7 | `L2/.../02_Selection` — 6 |
| 8 | `L2/.../03_Iteration` — 6 |

Then redo an early folder from memory, blank file, no peeking.

---

## 7. Git

All of `~/computational` is one repo — L1, L2, assignments, everything. End of
each session:

```bash
cd ~/computational
git add -A
git commit -m "Day 6: boolean conditions"
git push
```

`git status` shows what changed. `git log --oneline` shows your streak.

Not pushing yet — GitHub login still to do (`gh auth login`). Until then
`commit` works fine and saves your work locally.

---

## Notes

- Reference: `L1/OUTLINE.md` and the PDFs beside it.
- Each topic folder has its own `README.md` — read it before starting.
- Project briefs: `assignments/ASSIGNMENTS.md`.

---

## Optional: IPython, a scratchpad

Not needed for the course — for when you just want to test one idea without
making a file. It comes with Anaconda.

```bash
ipython
```

The prompt becomes `In [1]:`. It shows answers without `print()`:

```python
In [1]: year = 2024

In [2]: year % 4 == 0
Out[2]: True
```

Variables stay in memory between lines, so `year` is still there on the next one.

- `↑` — bring back a previous line
- `Tab` — complete a name
- `%reset` then `y` — forget all variables
- `exit` or `Ctrl+D` — back to `❯`

It handles pasted blocks better than plain `>>>`. But nothing you type here is
saved — for the exercises, edit the file and re-run it.
