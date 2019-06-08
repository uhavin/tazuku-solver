from fillers import (
    complete_ones,
    complete_zeros,
    fill_between,
    fill_left_of_double,
    fill_right_of_double,
)


_ = None

# grid_8 = [
#     [0, _, _, 0, _, 1, _, _],
#     [_, _, 1, _, _, _, _, 1],
#     [_, _, _, _, 0, _, 0, _],
#     [_, _, _, _, _, _, _, _],
#     [_, _, _, _, _, _, _, _],
#     [_, _, _, _, 0, 0, _, _],
#     [0, _, _, _, 1, _, 1, _],
#     [_, 1, _, 1, _, _, _, 1],
# ]


def test_complete_ones():
    line = [_, _, 0, 0, _, 0, 1, 0]
    complete_ones(line)
    assert [1, 1, 0, 0, 1, 0, 1, 0] == line


def test_complete_zeros():
    line = [_, 1, _, 1, _, 0, 1, 1]
    complete_zeros(line)
    assert [0, 1, 0, 1, 0, 0, 1, 1] == line


def test_fill_ones_between_zeros():
    line = [_, _, _, _, 0, _, 0, _]
    fill_between(line)
    assert [_, _, _, _, 0, 1, 0, _] == line


def test_fill_zeros_between_ones():
    line = [1, _, 1, _, 1, 0, 1, _]
    fill_between(line)
    assert [1, 0, 1, 0, 1, 0, 1, _] == line


def test_fill_left_of_double():
    line = [_, 0, 0, _, _, _, 0, 0]
    fill_left_of_double(line)
    assert [1, 0, 0, _, _, 1, 0, 0] == line


def test_fill_right_of_double():
    line = [0, 0, _, _, _, 0, 0, _]
    fill_right_of_double(line)
    assert [0, 0, 1, _, _, 0, 0, 1] == line
