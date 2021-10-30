import queue as qu

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def initBST(vals):
    queue = qu.Queue()
    for val in vals:
        queue.put(val)

    root = TreeNode(queue.get())

    node_queue = qu.Queue()
    node_queue.put(root)

    while not queue.empty() and not node_queue.empty():
        current = node_queue.get()

        left = queue.get()
        if left is not None:
            left = TreeNode(left)
            node_queue.put(left)
        current.left = left

        if queue.empty():
            continue

        right = queue.get()
        if right is not None:
            right = TreeNode(right)
            node_queue.put(right)
        current.right = right

    return root


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root == None:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)





if __name__ == '__main__':
    sol = Solution()

    vals = [1, None, 2, 3]

    root = initBST(vals)

    output = sol.inorderTraversal(root)

    print(output)
