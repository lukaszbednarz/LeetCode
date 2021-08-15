def hammingDistance(x: int, y: int) -> int:

    n = x ^ y
    bits = 0
    while n:
        bits += 1
        n = n & (n-1)

    return bits
