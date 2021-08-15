from ValidateBST import TreeNode

def isSymmetric(root: TreeNode) -> bool:

    if not root:
        return True

    nodes_l = []
    nodes_r = []
    curr_l = root
    curr_r = root

    while curr_l or nodes_l:

        while curr_l or curr_r:
            if curr_l is None or curr_r is None:
                return False
            if curr_l.val != curr_r.val:
                return False
            nodes_l.append(curr_l)
            nodes_r.append(curr_r)
            curr_l = curr_l.left
            curr_r = curr_r.right

        curr_l = nodes_l.pop()
        curr_r = nodes_r.pop()

        if curr_l.val != curr_r.val:
            return False

        curr_l = curr_l.right
        curr_r = curr_r.left


    return True






