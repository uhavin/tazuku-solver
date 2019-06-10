from helpers import stringify


def fill_where_three_nones(line):
    if line.count(None) != 3:
        return
    half = len(line) / 2

    if line.count(0) == half - 2:
        fill_value = 0
    elif line.count(1) == half - 2:
        fill_value = 1
    else:
        return

    line_str = stringify(line)
    value_blank_blank = line_str.find(f"{fill_value}__")
    blank_value_blank = line_str.find(f"_{fill_value}_")
    blank_blank_value = line_str.find(f"__{fill_value}")

    uncertain_nones = None
    certain_positions = set()

    if value_blank_blank >= 0:
        uncertain_nones = [value_blank_blank + 1, value_blank_blank + 2]
        certain_positions.add(_get_certain_position(line, uncertain_nones))
    if blank_value_blank >= 0:
        uncertain_nones = [blank_value_blank, blank_value_blank + 2]
        certain_positions.add(_get_certain_position(line, uncertain_nones))
    if blank_blank_value >= 0:
        uncertain_nones = [blank_blank_value, blank_blank_value + 1]
        certain_positions.add(_get_certain_position(line, uncertain_nones))

    for i in certain_positions:
        line[i] = fill_value


def fill_where_four_nones(line):
    if line.count(None) != 4:
        return
    half = len(line) / 2
    if line.count(0) == half - 1:
        fill_value = 1
    elif line.count(1) == half - 1:
        fill_value = 0
    else:
        return
    line_str = stringify(line)
    gap_of_four = line_str.find("____")
    if gap_of_four == -1:
        return

    certain_positions = [gap_of_four, gap_of_four + 3]

    for i in certain_positions:
        line[i] = fill_value


def _get_certain_position(line, uncertain_nones):
    for i, value in enumerate(line):
        if value is None and i not in uncertain_nones:
            return i
