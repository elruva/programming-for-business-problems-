# Programming for Business Problems

Coursework for a 13-session summer course in Python: from `print()` and
variables through to regular expressions, web scraping, pandas and simulation.

Everything here is my own work through the exercises, plus the lecture
materials they go with.

## Layout

```
lectures/       one folder per session — slides + exercise repo
assignments/    the three practical projects
exam_2024/      past exam paper
PRACTICE.md     my daily practice routine
```

Each lecture folder holds the session's slide deck and the exercise repo
cloned from the course org, for example:

```
lectures/L5/
├── Session 5 - Regular Expressions.pdf
└── 05-regex-elruva/
    └── 01_Regex_Exercises/    01_predict.py … 10_make.py
```

## How the exercises work

The course uses **PRIMM** — each topic runs through the same five stages, and
the filename says which one you're in:

| File | Stage | What you do |
|---|---|---|
| `01_predict.py` | **P**redict | Read the code, write down what you think it prints |
| — | **R**un | Run it and compare against your prediction |
| `05_investigate.py` | **I**nvestigate | Find the bug, explain the error message |
| `07_modify.py` | **M**odify | Change the code to do something new |
| `09_make.py` | **M**ake | Write it yourself from scratch |

Answers live as comments inside the `.py` files, under each `# Answer:` line.

## Sessions

| # | Date | Topic |
|---|---|---|
| 1 | Mon 27-07 | Intro, Python Basics |
| 2 | Tue 28-07 | Flow Control |
| 3 | Wed 29-07 | Functions |
| 4 | Thu 30-07 | Data Structures |
| 5 | Fri 31-07 | Practical Projects 1 |
| 6 | Mon 03-08 | Pattern Matching (regex) |
| 7 | Tue 04-08 | Web Scraping |
| 8 | Wed 05-08 | Web Scraping 2 — hidden APIs |
| 9 | Thu 06-08 | Data Analysis with Pandas |
| 10 | Fri 07-08 | Practical Project 2 |
| 11 | Mon 10-08 | Simple Simulation Models |
| 12 | Tue 11-08 | Discrete Event Simulation |
| 13 | Wed 12-08 | Practical Projects 3 |

## Running the code

```bash
cd lectures/L5/05-regex-elruva/01_Regex_Exercises
python 01_predict.py
```

Python 3.13 (Anaconda). `PRACTICE.md` has the full routine and the
things that usually go wrong.
