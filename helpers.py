def _stringify(line):
    line_str = ["_" if value is None else str(value) for value in line]
    return "".join(line_str)
