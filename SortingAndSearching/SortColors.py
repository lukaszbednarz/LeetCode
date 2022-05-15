from typing import List


class Solution:

    def swap(self, nums: List[int], i: int, j: int):

        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if n == 0:
            return None

        front = 0
        back = n - 1

        while (front < back) & (i <= back) :

            # put zero at the front
            if (nums[fr] == 2) & (back != i):
                self.swap(nums, i, back)
                back -= 1

            if (nums[i] == 0) & (front != i):
                self.swap(nums, i, front)
                front += 1

            if nums[back] == 0 and back != front:
                self.swap(nums, front, back)
                front += 1



            while front < back and nums[front] == 0:
                front += 1

            while back > 0 and nums[back] == 2:
                back -= 1

            i += 1
            while i < front:
                i += 1





