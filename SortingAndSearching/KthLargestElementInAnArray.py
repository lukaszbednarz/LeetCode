import bisect
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        tops = []

        for n in nums:
            print(tops)
            bisect.insort_right(tops, -n)
            if len(tops) > k:
                tops.pop()
        print(tops)

        return -tops[k - 1]


if __name__ == "__main__":

    solution = Solution()

    nums = [3,2,1,5,6,4]
    k = 2

    rsp = solution.findKthLargest(nums, k)
    print(rsp)
