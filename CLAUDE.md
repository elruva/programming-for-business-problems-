# computational

Course materials and coursework for a computational / programming course.

## Layout

- `PRACTICE.md` — the daily practice routine (PRIMM loop, schedule, troubleshooting)
- `github/README.md` — the user's own git/GitHub command notes
- `assignments/ASSIGNMENTS.md` — briefs for the three practical projects (lectures
  5, 10 and 13). **Read before working on any project**; each project's scope is
  limited to the lectures before its date.
- `lectures/` — lecture materials, one folder per lecture (see navigation below)
- `assignments/assignment-1-elruva/` — the cloned course repo for assignment 1
- `exam_2024/` — past exam paper and its task files
- `.claude/skills/` — project-scoped Claude Code skills
- `.claude/settings.local.json` — local Claude Code settings

## Navigating `lectures/`

Every lecture folder holds the same two things: the **session slide PDF**, and the
**cloned exercise repo** (named `0n-topic-elruva`). Inside the repo, numbered
subfolders group the exercises by topic, and every subfolder runs its own PRIMM
cycle — `NN_predict.py` → `NN_investigate.py` → `NN_modify.py` → `NN_make.py`,
numbered in the order you work them.

```
lectures/L4/
├── Session 4 - Data Structures.pdf     ← the slides
└── 04-data-structures-elruva/          ← the exercises (work here)
    ├── README.md                       ← what the session covers
    ├── 01_Lists/  02_Dictionaries/  03_StringMethods/  04_Files/
    └── each holding 01_predict.py … NN_make.py
```

| Lecture | Exercise repo | Subfolders | `.py` files |
|---|---|---|---|
| `L1` | `01-python-basics` | `01_Output` `02_Variables` `03_Input` `04_Math` `05_Modify_Make` | 26 |
| `L2` | `02-flow-control-elruva` | `01_Boolean_Conditions` `02_Selection` `03_Iteration` | 17 |
| `L3` | `03-functions-elruva` | `01_Function_Basics` `02_Parameters` `03_Return_Values` `04_Modules` `05_Error_Handling` `06_Make` | 22 |
| `L4` | `04-data-structures-elruva` | `01_Lists` `02_Dictionaries` `03_StringMethods` `04_Files` | 35 |
| `L5` | `05-regex-elruva` | `01_Regex_Exercises` | 10 |

Two exceptions to the pattern:

- **`L1`** holds *two* slide decks — `Session 0 - Introduction.pdf` and
  `Session 1 - Python Basics.pdf` — because lecture 1 covered both. It also has
  an `OUTLINE.md`, and its exercise folder is a ZIP copy with no git remote.
- **`L5`** contains the regex repo (`05-regex-elruva`), even though lecture 5 on
  the schedule below is Practical Projects 1. The course numbers its repos by
  deck, and regex is taught in lecture 6 — filed under `L5` to match the repo
  name. Both had happened by 05-08-2026, so nothing is out of bounds.

The remaining lectures (L6–L13) have no folders yet; create them as the sessions
happen.

## Conventions

- New lecture material goes in `lectures/L<n>/`.
- Source slides are PDFs; keep the original course filenames.
- Assignment work goes in `assignments/`, one subfolder per assignment.

## Course schedule

13 lectures, 9 am – 1 pm. **The `#` column matches the folder name**: lecture *n*
lives in `lectures/L<n>/`. Note that slide decks are numbered by *session*, not
lecture — lecture 1 covered both "Session 0 – Introduction" and "Session 1 –
Python Basics", so both PDFs sit in `L1/`. File by lecture number, not deck name.

| # | Date | Topic | Introduces |
|---|---|---|---|
| 1 | Mon 27-07-2026 | Intro, Python Basics | `print()`, strings, variables, `input()`, arithmetic |
| 2 | Tue 28-07-2026 | Flow Control | Booleans, `if`/`elif`/`else`, `while`, counters |
| 3 | Wed 29-07-2026 | Functions | `def`, arguments, `return` |
| 4 | Thu 30-07-2026 | Data Structures | lists, indexing, list methods, dictionaries |
| 5 | Fri 31-07-2026 | Practical Projects 1 | combines week 1 |
| 6 | Mon 03-08-2026 | Pattern Matching | regular expressions, `re` |
| 7 | Tue 04-08-2026 | Web Scraping | HTML/XML, BeautifulSoup |
| 8 | Wed 05-08-2026 | Web Scraping 2 | hidden APIs |
| 9 | Thu 06-08-2026 | Data Analysis with Pandas | Series, DataFrame, cleaning, Matplotlib |
| 10 | Fri 07-08-2026 | Practical Project 2 | combines days 1–9 |
| 11 | Mon 10-08-2026 | Simple Simulation Models | randomness, simulating events/markets |
| 12 | Tue 11-08-2026 | Discrete Event Simulation | SimPy |
| 13 | Wed 12-08-2026 | Practical Projects 3 | combines everything |

## Instructions for Claude

**Never use a Python construct before the lecture that introduces it.** Check
today's date against the schedule above and stay within what has been taught.
This is the most important rule here — a technically better answer that uses an
unfamiliar construct is a worse answer in this course.

- Before lecture 2: no `if`, no loops. Straight-line code only.
- Before lecture 3: no `def`, no `return`.
- Before lecture 4: no lists, no dictionaries, no indexing into collections.
- Never: comprehensions, `lambda`, `enumerate`/`zip`, f-string format specs,
  ternary expressions, or any library not introduced in a lecture — unless the
  user explicitly asks to go beyond the syllabus.

When working on exercises:

- Follow PRIMM. On `_predict.py` files, offer the prediction as something to
  check against, not as the answer to copy. Encourage running the code first.
- Write answers **as comments inside the `.py` file**, under each `# Answer:`
  line. Keep them to one short sentence in plain language — no jargon the
  lectures have not used.
- On `_investigate.py` files, actually run the file and quote the real error
  message. Some shipped files have no bug (e.g. `01_Output/04`, `05`); in that
  case answer for the bug described in the folder `README.md` and say so.
- On `_modify.py` and `_make.py`, use the simplest construction that works, and
  leave anything personal (name, favourite number) as an obvious placeholder.
- Explain errors by their last line first — that is where Python names the
  problem.

## Environment

- **Run Python with `python`, not `python3`.** `python` is Anaconda 3.13.9;
  `python3` resolves to a separate Homebrew 3.14 install because Homebrew
  precedes Anaconda on `PATH`.
- Exercises follow the PRIMM framework (Predict → Run → Investigate → Modify →
  Make). Answers are written as comments inside the exercise files themselves —
  don't strip them.
- `pdftotext` (poppler, via Homebrew) is available for reading the lecture PDFs.
