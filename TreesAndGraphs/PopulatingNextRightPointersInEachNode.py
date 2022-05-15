# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional, List

from TreesAndGraphs.ValidateBST import Node


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if root is None:
            return root

        dq = deque([root])
        ans = []

        while dq:

            dq_len = len(dq)


            prev = None

            for i in range(dq_len):

                curr = dq.popleft()

                if prev is not None:
                    prev.next = curr

                prev = curr


                ans.append(curr.val)

                if curr.left is not None:
                    dq.append(curr.left)

                if curr.right is not None:
                    dq.append(curr.right)

            ans.append("#")

        print(ans)
        return root
