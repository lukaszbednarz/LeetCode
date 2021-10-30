from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    out = ""

    for i in range(len(strs[0])):
        prev = strs[0][i]

        for s in strs[1:]:
            if i >= len(s) or s[i] != prev:
                return (out)

        out += prev

    return out