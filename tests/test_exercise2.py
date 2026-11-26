import exercise2


def test_is_passing_includes_grade_five():
    assert exercise2.is_passing(5) is True


def test_password_accepts_eight_characters_with_digit():
    assert exercise2.is_valid_password("abcdefg1") is True


def test_clamp_uses_high_as_upper_bound():
    assert exercise2.clamp(15, 0, 10) == 10
