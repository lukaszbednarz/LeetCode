import math as mt


def isPowerOfThree(n: int) -> bool:
    if n == 0:
        return False

    exponent = round(mt.log(n, 3), 6)

    if 3 ** exponent == n:
        return True
    else:
        return False
