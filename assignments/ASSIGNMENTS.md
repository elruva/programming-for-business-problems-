# Assignments

Three assignments, one per week of the course. Briefs below are as given by the
instructor.

---

## Assignment 1 — Python Fundamentals

- **Lecture:** 5 · Fri 31-07-2026 ("Practical Projects 1")
- **Due:** *(unknown)*
- **Code folder:** *(add path once the repo is cloned)*

### Brief

> Write a program that implements logic (selection statements) using functions
>
> Read and write data (e.g., csv files) and process user inputs

### Scope — what this needs

| Requirement | Taught in |
|---|---|
| Selection statements (`if` / `elif` / `else`) | Lecture 2 · Tue 28-07 |
| Functions (`def`, arguments, `return`) | Lecture 3 · Wed 29-07 |
| Process user inputs (`input()`, `int()`/`float()`) | Lecture 1 · Mon 27-07 |
| Lists and dictionaries for holding rows | Lecture 4 · Thu 30-07 |
| Read and write files (CSV) | **not in any lecture's learning goals** — see note |

**Note on CSV:** file reading/writing is not listed in the syllabus for lectures
1–5. Either it gets introduced in class without appearing in the goals, or the
`csv` module / `open()` is expected to be picked up independently. Ask the
instructor if unsure. Keep it simple when it comes up: `open()` with `read()` /
`write()`, or the `csv` module — not Pandas, which is not taught until lecture 9.

### Notes

---

## Assignment 2 — Webscraping

- **Lecture:** 10 · Fri 07-08-2026 ("Practical Project 2")
- **Due:** *(unknown)*
- **Code folder:** *(add path once the repo is cloned)*

### Brief

> Extract data from a website (e.g., Wikipedia, stock prices, rental rates,
> real-estate prices)
>
> Implement a program that uses the extracted data (e.g., calculate descriptive
> statistics, present the information to the user, visualize the data)

### Scope — what this needs

| Requirement | Taught in |
|---|---|
| HTML/XML structure, BeautifulSoup, single-page scraping | Lecture 7 · Tue 04-08 |
| Hidden APIs, for harder targets | Lecture 8 · Wed 05-08 |
| Regular expressions, for cleaning extracted text | Lecture 6 · Mon 03-08 |
| Descriptive statistics, DataFrames, cleaning | Lecture 9 · Thu 06-08 |
| Visualisation (Pandas + Matplotlib) | Lecture 9 · Thu 06-08 |
| Presenting results to the user | Lecture 1 |

Pick the data source early — a site that is easy to scrape makes the rest of the
assignment much easier. Wikipedia tables are the gentlest starting point.

### Notes

---

## Assignment 3 — Data Analytics and Simulation

- **Lecture:** 13 · Wed 12-08-2026 ("Practical Projects 3")
- **Due:** *(unknown)*
- **Code folder:** *(add path once the repo is cloned)*

### Brief

> Setup simulation models in Python (e.g., an inventory management problem, a
> supplier selection problem)
>
> Analyze the results of the simulation results

### Scope — what this needs

| Requirement | Taught in |
|---|---|
| Models and simulation, randomness, simulating events/markets | Lecture 11 · Mon 10-08 |
| Discrete-event simulation with SimPy | Lecture 12 · Tue 11-08 |
| Analysing results — statistics, DataFrames, plots | Lecture 9 · Thu 06-08 |

The two worked examples named in the brief — inventory management and supplier
selection — are both classic discrete-event problems, so SimPy (lecture 12) is
likely the intended tool.

### Notes

---

## How to use this file

- Paste any further instructions verbatim under the relevant **Brief** — do not
  summarise.
- Add the repo path under **Code folder** once each project repo is cloned.
- Use **Notes** for anything not in the brief: group members, what the instructor
  said in class, decisions made, problems hit.
- Each assignment only draws on lectures up to its own date. The **Scope** table
  is the limit for that assignment.
