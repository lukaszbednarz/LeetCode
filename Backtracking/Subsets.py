from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        resp = [[]]


        for n in nums:
            for i  in range(len(resp)):
                resp.append(resp[i] + [n])
                print(resp)

        return resp


if __name__ == "__main__":

    solution = Solution()
    input = [1, 2, 3]
    solution.subsets(input)