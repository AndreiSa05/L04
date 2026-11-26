"""Five progressively harder Python exercises for the L04 homework."""


def is_even(number):
    """Return True when number is divisible by two."""
    return number % 2 == 0


def count_vowels(text):
    """Return the number of vowels in text, ignoring letter case."""
    return sum(character.lower() in "aeiou" for character in text)


def second_largest(numbers):
    """Return the second-largest distinct number in numbers.

    Raise ValueError when fewer than two distinct values are provided.
    """
    distinct = sorted(set(numbers), reverse=True)
    if len(distinct) < 2:
        raise ValueError("at least two distinct numbers are required")
    return distinct[1]


def is_palindrome(text):
    """Return True when text reads the same forwards and backwards.

    Comparison ignores case and non-alphanumeric characters.
    """
    normalized = "".join(character.lower() for character in text if character.isalnum())
    return normalized == normalized[::-1]


def merge_intervals(intervals):
    """Merge overlapping inclusive intervals and return them in sorted order."""
    merged = []
    for start, end in sorted(intervals):
        if start > end:
            raise ValueError("interval start cannot be greater than its end")

        if not merged or start > merged[-1][1]:
            merged.append((start, end))
            continue

        previous_start, previous_end = merged[-1]
        merged[-1] = (previous_start, max(previous_end, end))

    return merged
