from ValidateBST import TreeNode
from typing import List
from collections import deque

def sortedArrayToBST(nums: List[int]) -> TreeNode:
    if len(nums) == 0:
        return None

    l = len(nums)
    split = int(l/2)

    root = TreeNode(nums[split])
    root.left = sortedArrayToBST(nums[:split])
    root.right = sortedArrayToBST(nums[split + 1:])

    return root
