# ============================================================
# 06_investigate.py - Notebook File Handling
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# ============================================================

import os

def load_notes(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.read().splitlines()
    return []

def save_notes(filename, notes):
    with open(filename, "w") as file:
        for note in notes:
            file.write(note + "\n")

def display_notes(notes):
    if not notes:
        print("No notes yet.")
    else:
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")

# Main program
notebook_file = "04_Files/notebook.txt"
notes = load_notes(notebook_file)

print("=== My Notebook ===")
display_notes(notes)

new_note = input("\nAdd a note (or press Enter to skip): ")
if new_note:
    notes.append(new_note)
    save_notes(notebook_file, notes)
    print("Note saved!")

# ============================================================
# QUESTIONS
# ============================================================

# Q1: Why does load_notes() check if the file exists before opening it?
# Answer: Opening a missing file gives a FileNotFoundError, so on the first run it returns an empty list instead.

# Q2: What does splitlines() do and why is it used here?
# Answer: It cuts the whole text into a list of lines, one note per line, without the "\n".

# Q3: In save_notes(), why do we add "\n" after each note?
# Answer: write() does not add a new line, so without it all notes would end up on one line.

# Q4: What would happen if we used "a" instead of "w" in save_notes()?
# Answer: "a" adds to the end instead of overwriting, so every old note would be written again each save.

# Q5: Why does enumerate() use the parameter 1 in display_notes()?
# Answer: So the numbering starts at 1 instead of 0, which reads better for a person.
