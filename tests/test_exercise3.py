import exercise3


def test_average_empty_list_is_zero():
    assert exercise3.average([]) == 0


def test_first_word_empty_text_is_empty():
    assert exercise3.first_word("") == ""


def test_percent_zero_total_is_zero():
    assert exercise3.percent(1, 0) == 0
