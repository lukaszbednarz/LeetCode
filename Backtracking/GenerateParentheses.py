from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ret = set()

        def backtrack(currStr):
            print(currStr)
            print(ret)

            if len(currStr) == n * 2:
                ret.add(currStr)
                return

            if len(currStr) == 0:
                backtrack("()")
            else:
                i = 1
                while i <= (n - len(currStr) // 2):
                    for l in self.generateParenthesis(i):
                        backtrack(currStr + l)
                        backtrack(l + currStr)
                    backtrack("(" + currStr + ")")
                    i += 1

        backtrack("")

        return list(ret)



if __name__ == "__main__":

    solution = Solution()

    input = 3

    res = solution.generateParenthesis(input)

    print(res)