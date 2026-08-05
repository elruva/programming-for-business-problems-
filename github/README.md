# Git & GitHub — my command notes

Everything here is run from the repo folder. Start every session with:

```bash
cd ~/computational
```

This repo lives at <https://github.com/elruva/programming-for-business-problems->.

---

## The daily loop

Four commands, in this order. This is 95% of git.

```bash
git status                # 1. what have I changed?
git add -A                # 2. stage everything
git commit -m "message"   # 3. save it locally, with a note
git push                  # 4. send it to GitHub
```

| Command | What it does |
|---|---|
| `git status` | Modified files, untracked files, whether I'm ahead of GitHub. Run it constantly. |
| `git add -A` | Marks changes for the next commit. `-A` = everything. |
| `git commit -m` | Records a snapshot **on my machine only**. Nothing is online yet. |
| `git push` | Uploads commits to GitHub. Now it's online. |

Commit when I finish something coherent — a folder of exercises, a session's
work. Push at the end of the day.

### Staging only part of it

```bash
git add lectures/L5                  # one folder
git add lectures/L5/05-regex-elruva/01_Regex_Exercises/01_predict.py   # one file
```

---

## Pulling

```bash
git pull        # fetch GitHub's version and merge it into mine
```

Rarely needed with one laptop and one person — `pull` only has something to do
when GitHub has commits my machine doesn't (edited a file in the browser, worked
from another computer).

Habit worth keeping anyway: **pull before starting, push when finished.**

---

## Looking around

```bash
git log --oneline -10   # last 10 commits, one line each
git diff                # changed but not staged
git diff --staged       # staged but not committed
git show                # full contents of the last commit
```

`git diff` before committing is the last chance to spot a leftover debug
`print()`.

---

## Undoing

```bash
git restore FILE               # throw away my edits — PERMANENT, no undo
git restore --staged FILE      # unstage, keep the edits
git commit --amend -m "better" # reword the last commit (only if not pushed yet)
```

`git restore` really destroys work. Almost everything else in git is
recoverable; that one isn't.

---

## .gitignore

A list of files git should pretend it can't see. They stay on my disk and open
normally — git just never tracks them, and they never reach GitHub.

Lives at the repo root: `~/computational/.gitignore`

| Pattern | Matches |
|---|---|
| `notes.txt` | that name, **anywhere** in the repo |
| `*.pyc` | any file ending `.pyc` |
| `.claude/` | that folder and everything inside it |
| `/notes.txt` | only at the repo root |
| `04_Files/*.csv` | every `.csv` in that folder |
| `lectures/L4/…/newdata.csv` | that exact file, nothing else |
| `!keep.log` | exception — un-ignore this |
| `# text` | a comment |

**A pattern with a slash is anchored** to the folder holding the `.gitignore`.
No slash means it floats and matches at any depth. A trailing `/` means "folder
only".

Rule of thumb: **track the thing that produces a file, not the file it
produces.** The `.py` exercise is work; the `report.txt` it writes is output.

### The trap

`.gitignore` only affects files git isn't **already tracking**. Adding a name
after it's been committed does nothing — it keeps showing up and stays on
GitHub. To actually stop tracking it:

```bash
git rm --cached FILE          # untrack, but keep it on my disk
git rm -r --cached FOLDER     # same for a folder
```

Then commit and push.

### Which rule is hiding my file?

```bash
git check-ignore -v path/to/file
```

Prints the exact `.gitignore` line to blame. Useful when a file refuses to be
added.

### Secrets

Git history is permanent. If a password gets committed, adding it to
`.gitignore` afterwards changes nothing — it's still in the old commit, and this
repo is public. Keys go in a file called `.env`, and `.env` goes in
`.gitignore` **before** the first commit.

---

## Setup, for reference

Already done for this repo, but this is what it took:

```bash
git init                                    # start tracking a folder
git remote add origin https://github.com/elruva/programming-for-business-problems.git
git push -u origin main                     # first push, -u links the branches
```

After that first `-u` push, plain `git push` is enough.

---

## When something looks wrong

```bash
git status              # almost always answers it
git log --oneline -5    # what did I actually commit?
git remote -v           # am I pointed at the right GitHub repo?
```
