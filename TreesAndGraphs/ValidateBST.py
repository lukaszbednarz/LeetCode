import queue as qu

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, next: 'Node' = None, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.next = next


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

        if not queue.empty():
            right = queue.get()
            if right is not None:
                right = TreeNode(right)
                node_queue.put(right)
            current.right = right

    return root




def isValidBST(root: TreeNode) -> bool:
    if root is None:
        return True

    if root.left is not None:
        if root.left.val >= root.val or not isValidBST(root.left):
            return False
    if root.right is not None:
        if root.right.val <= root.val or not isValidBST(root.right):
            return False

    return True

def isValidBST2(root: TreeNode) -> bool:
    return _isValidBST(root)

def _isValidBST(root: TreeNode, min_val = None, max_val = None) -> bool:
    if root is None:
        return True

    # if min_val is None:
    #     min_val = root.val
    # else:
    #     min_val = min(min_val, root.val)
    #
    # if max_val is None:
    #     max_val = root.val
    # else:
    #     max_val = max(max_val, root.val)

    if root.left is not None:
        if root.left.val >= root.val \
            or (min_val is not None and root.left.val <= min_val)\
                or not _isValidBST(root.left,
                                    min_val = min_val,
                                    max_val = root.val):
            return False
    if root.right is not None:
        if root.right.val <= root.val \
            or (max_val is not None and root.right.val >= max_val) \
                or not _isValidBST(root.right,
                                min_val = root.val,
                                max_val = max_val):
            return False

    return True



class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        if root.left is not None:
            if root.left.val >= root.val or not isValidBST(root.left):
                return False
        if root.right is not None:
            if root.right.val <= root.val or not isValidBST(root.right):
                return False

        return True
