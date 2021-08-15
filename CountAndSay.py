
def countAndSay(n: int) -> str:
    if n == 1:
        return("1")
    else:
        s = countAndSay(n - 1)
        return rle(s)

def rle(s: str) -> str:

    curr = s[0]
    count = 0

    out = ""

    for i in range(len(s)):
        if(s[i] == curr):
            count += 1
        else:
            out += str(count) + str(curr)
            count = 1
            curr = s[i]

    out += str(count) + str(curr)

    return out

