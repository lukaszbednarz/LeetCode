class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        dq = deque(tokens)

        while dq:

            left = int(dq.popleft())

            if not dq:
                return left

            right = int(dq.popleft())

            op = dq.popleft()

            while op not in ["+", "-", "*", "/"]:
                temp = left
                left = right
                right = int(op)
                op = dq.popleft()
                dq.appendleft(temp)

            if op == "+":
                res = left + right
            elif op == "-":
                res = left - right
            elif op == "*":
                res = left * right
            elif op == "/":
                res = left / right
            else:
                raise Exception(f"unknown op: {op}")

            dq.appendleft(res)


if __name__ == "__main__":

    solution = Solution()

    a = 1
    b = 2

    resp = solution.getSum(a, b)

    print(resp)
