# Bug reports for exercise3.py

Line: 3
Problem: `average` divides by the length of an empty list even though its docstring says an empty list has average 0.
Example: `average([])` raises ZeroDivisionError, expected 0.
Fix: `return sum(numbers) / len(numbers) if numbers else 0`

Line: 8
Problem: `first_word` indexes an empty split result even though its docstring says empty text returns an empty string.
Example: `first_word("")` raises IndexError, expected `""`.
Fix: `return text.split()[0] if text.split() else ""`

Line: 13
Problem: `percent` divides by zero even though its docstring says a zero total returns 0.
Example: `percent(1, 0)` raises ZeroDivisionError, expected 0.
Fix: `return part / total * 100 if total else 0`
