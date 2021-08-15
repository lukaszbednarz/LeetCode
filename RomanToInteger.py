rom2int = {"M": 1000,
           "D": 500,
           "C": 100,
           "L": 50,
           "X": 10,
           "V": 5,
           "I": 1}
int2rom = {1000: "M",
           500: "D",
           100: "C",
           50: "L",
           10: "X",
           5: "V",
           1: "I"}

def romanToInt( s: str) -> int:

    if len(s) == 0:
        return 0

    res = 0
    prev = rom2int[s[-1]]

    for i in range(len(s) -1, -1, -1):

        curr = rom2int[s[i]]
        if (curr < prev):
            curr = - curr
        res += curr
        prev = curr

    return res

