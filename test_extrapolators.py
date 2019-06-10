import pytest

from guessers import fill_certain_ones, fill_certain_zeros

_ = None


fill_certain_one_cases = [
    ([0, 1, _, _, _, 0, 1, 0, 1, 0], [0, 1, _, _, 1, 0, 1, 0, 1, 0]),
    ([0, 0, _, _, 1, 0, 1, 0, 1, _], [0, 0, _, _, 1, 0, 1, 0, 1, 1]),
    ([0, 0, _, 1, _, 0, 1, 0, _, 1], [0, 0, _, 1, _, 0, 1, 0, 1, 1]),
    ([0, 1, _, _, _, 1, 0, 0, 1, 0], [0, 1, 1, _, 1, 1, 0, 0, 1, 0]),
    ([0, 1, _, _, 1, _, 0, 0, 1, 0], [0, 1, 1, _, 1, 1, 0, 0, 1, 0]),
]


@pytest.mark.parametrize("line,solution", fill_certain_one_cases)
def test_fill_certaion_ones(line, solution):
    fill_certain_ones(line)
    assert solution == line


fill_certain_zero_cases = [
    ([1, 0, _, _, _, 1, 0, 1, 0, 1], [1, 0, _, _, 0, 1, 0, 1, 0, 1]),
    ([1, 1, _, _, 0, 1, 0, 1, 0, _], [1, 1, _, _, 0, 1, 0, 1, 0, 0]),
    ([1, 1, _, 0, _, 1, 0, 1, _, 0], [1, 1, _, 0, _, 1, 0, 1, 0, 0]),
    ([1, 0, _, _, _, 0, 1, 1, 0, 1], [1, 0, 0, _, 0, 0, 1, 1, 0, 1]),
    ([1, 0, _, _, 0, _, 1, 1, 0, 1], [1, 0, 0, _, 0, 0, 1, 1, 0, 1]),
]


@pytest.mark.parametrize("line,solution", fill_certain_one_cases)
def test_fill_certain_zeros(line, solution):
    fill_certain_zeros(line)
    assert solution == line
