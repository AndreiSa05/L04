# Bug reports for exercise2.py

Line: 3
Problem: `is_passing` rejects grade 5 even though the docstring says 5 or more.
Example: `is_passing(5)` returns False, expected True.
Fix: `return grade >= 5`

Line: 8
Problem: `is_valid_password` rejects passwords with exactly 8 characters, although the requirement is at least 8 characters.
Example: `is_valid_password("abcdefg1")` returns False, expected True.
Fix: `return len(password) >= 8 and any(c.isdigit() for c in password)`

Line: 12
Problem: `clamp` uses `low` as the upper bound, so values above the requested maximum are clamped incorrectly.
Example: `clamp(15, 0, 10)` returns 0, expected 10.
Fix: `return max(low, min(x, high))`
