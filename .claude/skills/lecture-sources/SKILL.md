---
name: lecture-sources
description: Find and read the source material for a lecture - slide PDFs, session code, outlines and folder READMEs - before answering questions or writing exercise code. Use when working on any lecture or assignment so the answer matches what was actually taught.
---

# Reading lecture sources

Before answering a course question or filling in exercise code, read what the
lecture actually taught. The slides are the authority on wording, examples and
scope — not general Python knowledge.

## Where the material lives

```
lectures/L<n>/                  lecture n (matches the # column in CLAUDE.md)
├── Session N - <Topic>.pdf     the slide deck
├── OUTLINE.md                  condensed notes, if already written
├── *.py                        session code shown in class, if provided
└── <exercise-repo>/            practice folders, each with its own README.md
```

`lectures/L<n>/` is numbered by **lecture**, not by slide deck. Lecture 1 holds
both "Session 0" and "Session 1" PDFs.

## How to read each source

**Read in this order** — cheapest and most relevant first:

1. `OUTLINE.md` in the lecture folder, if it exists. Already condensed.
2. The exercise folder `README.md` files. These list every file, its concepts,
   and a troubleshooting checklist.
3. Session `.py` files shipped with the lecture. These are the instructor's own
   examples — the best guide to expected style.
4. The slide PDF, for anything still unclear.

**Reading a PDF.** The Read tool cannot open these directly. Use `pdftotext`
(poppler, already installed via Homebrew):

```bash
pdftotext -layout "lectures/L1/Session 1 - Python Basics.pdf" -
```

`-layout` keeps columns and code blocks readable. Add `-f 5 -l 10` to limit to
pages 5–10 of a long deck. If `pdftotext` is missing: `brew install poppler`.

If a lecture has no `OUTLINE.md`, offer to write one after reading the PDF —
future sessions then start from step 1.

## Reusing lecture code in assignments

When writing exercise answers, prefer what the slides did:

- **Match the construct.** If the slides used two `print()` calls, don't reach
  for `\n` just because it is shorter. If they introduced f-strings, use
  f-strings rather than concatenation.
- **Match the vocabulary.** Reuse the slides' terms — "output statement",
  "string", "assign" — in explanation comments.
- **Reuse example shapes.** The slides' `num1 = 5 / num2 = 10 / result = num1 +
  num2 / print(result)` pattern is the model for arithmetic answers.
- **Never exceed the deck.** If a construct does not appear in the lecture PDF or
  session code up to that date, do not use it. Check the schedule in
  `CLAUDE.md`.

When an exercise mirrors a slide example, say so — "the slides do this on the
f-string slide" — so the connection is visible.

## Quick checks

- Which lecture is this exercise from? Match the folder to the schedule in
  `CLAUDE.md`.
- Does the folder `README.md` describe a bug the code does not actually have?
  Some shipped files are already correct — say so rather than inventing one.
- Does the exercise repeat a slide example? Reuse it rather than inventing new
  code.
