def reverseBits(n: int) -> int:

    ret =  0
    for i in range(32):
        ret = ret << 1
        ret += n & 1
        n = n >> 1

    return ret