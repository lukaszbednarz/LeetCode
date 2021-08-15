import re

def strStr(haystack: str, needle: str) -> int:
    if len(needle) < 1 :
        return 0

    regmatch = re.search(needle, haystack)

    if regmatch is None :
        return -1
    else:
        return regmatch.start()
