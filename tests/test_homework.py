import pytest

from homework import (
    count_vowels,
    is_even,
    is_palindrome,
    merge_intervals,
    second_largest,
)


def test_is_even():
    assert is_even(12) is True
    assert is_even(7) is False


def test_count_vowels():
    assert count_vowels("Hello World") == 3


def test_second_largest_handles_duplicates():
    assert second_largest([4, 9, 9, 2]) == 4


def test_second_largest_requires_two_distinct_values():
    with pytest.raises(ValueError):
        second_largest([5, 5])


def test_is_palindrome_ignores_case_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") is True


def test_merge_intervals():
    assert merge_intervals([(1, 3), (2, 6), (8, 10), (9, 12)]) == [
        (1, 6),
        (8, 12),
    ]
