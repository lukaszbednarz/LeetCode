from typing import List
def generate(numRows: int) -> List[List[int]]:

    out = []

    if numRows > 0:
        out.append([1])

    for i in range(numRows-1):
        curr = [1]
        for j in range(i):
            curr.append(prev[j] + prev[j + 1])
        curr.append(1)
        out.append(curr)
        prev = curr
    return out

