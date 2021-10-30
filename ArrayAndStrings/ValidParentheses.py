def isValid(s: str) -> bool:
    stack = []
    map = {"]": "[",
           "}": "{",
           ")": "("}

    for a in s:
        if stack and a in map.keys() and stack[-1] == map[a]:
            stack.pop()
        else:
            stack.append(a)

    if stack:
        return False
    else:
        return True


