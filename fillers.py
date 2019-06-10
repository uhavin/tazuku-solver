def complete_zeros(line):
    if line.count(1) != len(line) / 2:
        return
    for position, value in enumerate(line):
        if value is not None:
            continue
        line[position] = 0


def complete_ones(line):
    if line.count(0) != len(line) / 2:
        return
    for position, value in enumerate(line):
        if value is not None:
            continue
        line[position] = 1


def fill_between(line):
    for position, value in enumerate(line):
        fill_position = position + 1
        compare_position = position + 2
        if value is None:
            continue
        if line[fill_position] is not None:
            continue
        if compare_position >= len(line):
            continue
        if line[position] != line[compare_position]:
            continue
        line[fill_position] = (value + 1) % 2


def fill_left_of_double(line):
    for position, value in enumerate(line):
        fill_position = position - 1
        compare_position = position + 1

        if value is None:
            continue
        if fill_position < 0:
            continue
        if compare_position >= len(line):
            continue
        if line[position] != line[compare_position]:
            continue
        line[fill_position] = (value + 1) % 2


def fill_right_of_double(line):
    for position, value in enumerate(line):
        fill_position = position + 2
        compare_position = position + 1

        if value is None:
            continue
        if compare_position >= len(line):
            continue
        if line[position] != line[compare_position]:
            continue
        line[fill_position] = (value + 1) % 2
