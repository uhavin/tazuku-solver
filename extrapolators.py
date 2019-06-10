from helpers import _stringify


def fill_certain_zeros(line):
    half = len(line) / 2
    if line.count(1) != half - 1:
        return
    if line.count(0) != half - 2:
        return

    line_str = _stringify(line)
    one_blank_blank = line_str.find("0__")
    blank_one_blank = line_str.find("_0_")
    blank_blank_one = line_str.find("__0")

    uncertain_nones = None
    certain_positions = []

    if one_blank_blank >= 0:
        uncertain_nones = [one_blank_blank + 1, one_blank_blank + 2]
        certain_positions.append(_get_certain_position(line, uncertain_nones))
    if blank_one_blank >= 0:
        uncertain_nones = [blank_one_blank, blank_one_blank + 2]
        certain_positions.append(_get_certain_position(line, uncertain_nones))
    if blank_blank_one >= 0:
        uncertain_nones = [blank_blank_one, blank_blank_one + 1]
        certain_positions.append(_get_certain_position(line, uncertain_nones))

    for i in certain_positions:
        line[i] = 0


def fill_certain_ones(line):
    half = len(line) / 2
    if line.count(0) != half - 1:
        return
    if line.count(1) != half - 2:
        return

    line_str = _stringify(line)
    one_blank_blank = line_str.find("1__")
    blank_one_blank = line_str.find("_1_")
    blank_blank_one = line_str.find("__1")

    uncertain_nones = None
    certain_positions = []

    if one_blank_blank >= 0:
        uncertain_nones = [one_blank_blank + 1, one_blank_blank + 2]
        certain_positions.append(_get_certain_position(line, uncertain_nones))
    if blank_one_blank >= 0:
        uncertain_nones = [blank_one_blank, blank_one_blank + 2]
        certain_positions.append(_get_certain_position(line, uncertain_nones))
    if blank_blank_one >= 0:
        uncertain_nones = [blank_blank_one, blank_blank_one + 1]
        certain_positions.append(_get_certain_position(line, uncertain_nones))

    for i in certain_positions:
        line[i] = 1


def _get_certain_position(line, uncertain_nones):
    for i, value in enumerate(line):
        if value is None and i not in uncertain_nones:
            return i
