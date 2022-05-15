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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        left_to_right = True

        dq_ltr = deque([root])

        dq_rtl = deque()

        ans = []

        if root is None:
            return ans

        while dq_ltr or dq_rtl:

            ans.append([])

            if left_to_right:
                while dq_ltr:
                    curr = dq_ltr.pop()
                    ans[-1].append(curr.val)

                    if curr.left is not None:
                        dq_rtl.append(curr.left)

                    if curr.right is not None:
                        dq_rtl.append(curr.right)

            else:
                while dq_rtl:
                    curr = dq_rtl.pop()
                    ans[-1].append(curr.val)

                    if curr.right is not None:
                        dq_ltr.append(curr.right)

                    if curr.left is not None:
                        dq_ltr.append(curr.left)

            # switch direction
            left_to_right = not left_to_right

        return ans
