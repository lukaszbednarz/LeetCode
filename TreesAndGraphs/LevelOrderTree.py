from ValidateBST import TreeNode
from typing import List
from queue import Queue

def levelOrder(root: TreeNode) -> List[List[int]]:
    if root is None:
        return []

    vals = []
    nodes = Queue()
    nodes.put(root)
    children = Queue()

    level_vals = []
    while not nodes.empty():
        curr = nodes.get()
        level_vals.append(curr.val)

        if curr.left:
            children.put(curr.left)
        if curr.right:
            children.put(curr.right)

        if nodes.empty():
            nodes = children
            children = Queue()
            vals.append(level_vals)
            level_vals = []

    return(vals)





def childrenValues(node: TreeNode) -> List[int]:
    if node is None:
        return None

    vals = []
    if not node.left and not node.right:
        return None

    if node.left:
        vals.append(node.left.val)
    else:
        vals.append(None)
    if node.right:
        vals.append(node.right.val)
    else:
        vals.append(None)

    return vals
