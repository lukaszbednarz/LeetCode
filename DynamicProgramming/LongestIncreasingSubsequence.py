from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = {nums[0]: 1}
        total_max = 1
        for e in nums:

            curr_keys = [*dp.keys()]
            max = 1
            for k in curr_keys:
                if e > k and dp[k] >= max:
                    max = dp[k] + 1

            dp[e] = max
            if max > total_max:
                total_max = max

        return total_max

    def lengthOfLIS2(self, nums: List[int]) -> int:
        import bisect
        ss = [nums[0]]

        for n in nums[1:]:
            if n < ss[-1]:
                i = bisect_left(ss, n)
                ss[i] = n
            elif n > ss[-1]:
                ss += [n]

        return len(ss)


if __name__ == '__main__':
    sol = Solution()

    nums = [10, 9, 2, 5, 3, 7, 101, 18]

    output = sol.lengthOfLIS2(nums)

    print(output)
