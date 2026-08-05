# Regex Exercises

Work through these exercises **after** the lecture, since the later tasks combine
basic patterns with quantifiers, character sets, and groups. Follow the usual
cycle: **predict → investigate → modify → make**.

## Exercises

| File | Type | Description |
|------|------|-------------|
| `01_predict.py` | Predict | `match()` vs `search()`, case sensitivity |
| `02_predict.py` | Predict | Anchors (`^` and `$`) for start/end matching |
| `03_predict.py` | Predict | Groups `()`, escaping, wildcards, `\d` |
| `04_predict.py` | Predict | Character sets `[A-Z]` and capture groups |
| `05_investigate.py` | Investigate | Where `match()`, `search()`, and anchors succeed or fail |
| `06_investigate.py` | Investigate | Greedy matching `.*`, optional parts `?`, sets with quantifiers |
| `07_modify.py` | Modify | Fix a URL pattern to match various URL formats |
| `08_modify.py` | Modify | Tighten a loose IP-address pattern (escaping, `{1,3}`, anchors) |
| `09_make.py` | Make | Extract `#hashtags` and `@mentions` from captions |
| `10_make.py` | Make | Validate product codes with sets, quantifiers, optional group |

## Key Concepts

- **`re.compile` / `match` / `search` / `findall`** - core `re` functions
- **Raw strings** - always write patterns as `r"..."`
- **Wildcards** - `.`, `\d`, `\w`, `\s` (and `\D`, `\W`, `\S`)
- **Anchors** - `^` start, `$` end, `\b` word boundary
- **Quantifiers** - `*`, `+`, `?`, `{n}`, `{n,m}`
- **Character sets** - `[abc]`, `[a-z]`, `[^abc]`
- **Groups & alternation** - `()` capture, `(a|b)` alternatives
- **Escaping** - `\.` for a literal dot, etc.

## Help! My Code Doesn't Work!

Make sure that you check for the following things:
- Import `re` and use raw strings `r"..."` for every pattern
- `match()` only checks the start of the string - use `search()` for anywhere
- `.` matches ANY character - escape it as `\.` for a literal dot
- `|` has low precedence - use `()` to group alternatives
- Anchor with `^` and `$` when the WHOLE string must match
- `None` from `.group(n)` means the match succeeded but that optional group was empty
