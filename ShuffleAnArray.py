from typing import List
import random as rd

class Solution:

    raw_nums: List[int]
    nums: List[int]

    def __init__(self, nums: List[int]):
        rd.seed(123)
        self.nums = nums


    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        tmp = self.nums.copy()
        rd.shuffle(tmp)

        return tmp