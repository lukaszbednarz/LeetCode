# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional, List

from TreesAndGraphs.ValidateBST import TreeNode


class Solution:

    def inOrderElements(self, root: Optional[TreeNode]):

        ans = []

        if root is None:
            return ans

        if root.left is not None:

            ans += self.inOrderElements(root.left)

        ans.append(root.val)

        if root.right is not None:
            ans += self.inOrderElements(root.right)

        return ans



    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # in order traversal

        ans = []

        if root is None:
            return ans


        return self.inOrderElements(root)[k - 1]

