
class MinStack:


    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        self._stack.append(val)

        _min = self.getMin()

        if _min is None:
           _min = val
        else:
            _min = min(val, _min)

        self._min_stack.append(_min)


    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()


    def top(self) -> int:
        if len(self._stack) == 0:
            return None

        return self._stack[-1]

    def getMin(self) -> int:

        if len(self._min_stack) == 0:
            return None

        return self._min_stack[-1]

