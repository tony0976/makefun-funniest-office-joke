"""Writes one funny office joke to /output/entry.txt."""
import os

TEXT = "HR said the new wellness initiative is a plant on every desk. Mine died in a week, which HR called 'a metaphor for burnout' and I called 'Tuesday'."

# Rule: the joke must be a single line of at most 200 characters.
assert "\n" not in TEXT and len(TEXT) <= 200, f"entry must be one line, <=200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
