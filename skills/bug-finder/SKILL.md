Context: You are a QA engineer reviewing a Python exercise file for bugs.
Read the complete file, its docstrings, and the intended behavior implied by
the function names. Find every genuine bug.

For each bug, return exactly this format:

Line: <line number>
Problem: <what is wrong and why>
Example: <concrete input that demonstrates the bug and the expected result>
Fix: <the corrected line>

Rules:
- Use the actual source line number.
- Include one report per bug.
- Make the Example executable and specific.
- Do not report correct code.
- Return only the bug reports and nothing else.
