# Bug reports for exercise1.py

Line: 3
Problem: The condition `n % 2 == 1` checks for odd numbers, not even numbers. For even numbers, the remainder when divided by 2 should be 0.
Example: is_even(4) returns False, expected True.
Fix: return n % 2 == 0

Line: 8
Problem: The function returns the sum of width and height, not the product, which is the correct formula for rectangle area.
Example: rectangle_area(3, 4) returns 7, expected 12.
Fix: return width * height

Line: 12
Problem: The function `double(n)` adds 2 to n, but the docstring says "twice the number n", which means it should multiply by 2.
Example: double(5) returns 7, expected 10.
Fix: return n * 2
