import pytest

from extrapolators import fill_where_three_nones, fill_where_four_nones

_ = None


test_cases_three_nones = [
    # with solution
    ([0, 1, _, _, _, 0, 1, 0], [0, 1, _, _, 1, 0, 1, 0]),
    ([0, 0, _, _, 1, 0, 1, 0, 1, _], [0, 0, _, _, 1, 0, 1, 0, 1, 1]),
    ([0, 0, _, 1, _, 0, 1, 0, _, 1], [0, 0, _, 1, _, 0, 1, 0, 1, 1]),
    ([0, 1, _, _, _, 1, 0, 0, 1, 0], [0, 1, 1, _, 1, 1, 0, 0, 1, 0]),
    ([0, 1, _, _, 1, _, 0, 0, 1, 0], [0, 1, 1, _, 1, 1, 0, 0, 1, 0]),
    ([1, 0, _, _, _, 1, 0, 1, 0, 1], [1, 0, _, _, 0, 1, 0, 1, 0, 1]),
    ([1, 1, _, _, 0, 1, 0, 1, 0, _], [1, 1, _, _, 0, 1, 0, 1, 0, 0]),
    ([1, 1, _, 0, _, 1, 0, 1, _, 0], [1, 1, _, 0, _, 1, 0, 1, 0, 0]),
    ([1, 0, _, _, _, 0, 1, 1, 0, 1], [1, 0, 0, _, 0, 0, 1, 1, 0, 1]),
    ([1, 0, _, _, 0, _, 1, 1, 0, 1], [1, 0, 0, _, 0, 0, 1, 1, 0, 1]),
    ([0, 1, _, _, 1, 0, 1, 0, 0, _], [0, 1, _, _, 1, 0, 1, 0, 0, 1]),
    # no solution
    ([0, 1, 1, _, _, 0, 1, 0, 1, 0], [0, 1, 1, _, _, 0, 1, 0, 1, 0]),
    ([0, 1, 1, _, _, 0, _, 0, _, 0], [0, 1, 1, _, _, 0, _, 0, _, 0]),
    ([0, 1, 0, _, _, 0, 1, 0, _, 1], [0, 1, 0, _, _, 0, 1, 0, _, 1]),
]


@pytest.mark.parametrize("line,expected_result", test_cases_three_nones)
def test_fill_where_three_nones(line, expected_result):
    fill_where_three_nones(line)
    assert expected_result == line


test_cases_four_nones = [
    ([1, 0, _, _, _, _, 0, 0, 1, 0], [1, 0, 1, _, _, 1, 0, 0, 1, 0]),
    ([0, 1, _, _, _, _, 1, 1, 0, 1], [0, 1, 0, _, _, 0, 1, 1, 0, 1]),
    ([0, 1, 1, _, _, 0, 1, 0, 1, 0], [0, 1, 1, _, _, 0, 1, 0, 1, 0]),
    ([0, 1, 1, _, _, 0, _, 0, _, 0], [0, 1, 1, _, _, 0, _, 0, _, 0]),
    ([0, 1, 0, _, _, 0, 1, 0, _, 1], [0, 1, 0, _, _, 0, 1, 0, _, 1]),
]


@pytest.mark.parametrize("line,solution", test_cases_four_nones)
def test_fill_where_four_nones(line, solution):
    fill_where_four_nones(line)
    assert solution == line
