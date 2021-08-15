import re

def myAtoi(s: str) -> int:

    s = re.sub("^\\s*([+-]?\\d+).*", "\\1", s, 1)

    if not re.match("[+-]?\\d+", s):
        return 0
    i = int(s)

    max_int = pow(2, 31) - 1
    min_int = -pow(2, 31)

    if i > max_int :
        return max_int
    if i <= min_int :
        return min_int

    return i