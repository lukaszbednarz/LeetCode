from typing import List

store = {}


def rob(nums: List[int]) -> int:

    while nums and nums[-1] == 0:
        nums.pop()

    i = 0
    while nums[-1] == 0:
        i += 1

    nums = nums[i:]

    l = len(nums)


    if l == 1:
        return nums[0]

    if l == 2:
        return max(nums)

    profit = store.get(l)

    if profit:
        return profit


    profit = max(nums[0] + rob(nums[2:]),
                 rob(nums[1:]))
    store[l] = profit

    return profit


class Solution:
    store = {}

    def rob(self, nums: List[int]) -> int:

        while nums and nums[-1] == 0:
            nums.pop()

        i = 0
        while nums[-1] == 0:
            i += 1

        nums = nums[i:]

        l = len(nums)

        if l == 0:
            return 0

        if l == 1:
            return nums[0]

        if l == 2:
            return max(nums)

        profit = self.store.get(l)

        if profit:
            return profit


        profit = max(nums[0] + self.rob(nums[2:]),
                     self.rob(nums[1:]))
        self.store[l] = profit

        return profit