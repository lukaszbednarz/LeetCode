from TreesAndGraphs.KthSmallest import Solution


# Press the green button in the gutter to run the script.
from TreesAndGraphs.ValidateBST import initBST

if __name__ == '__main__':

    nodes = [5,3,6,2,4,None,None,1]

    root = initBST(nodes)

    sol = Solution()

    ans = sol.kthSmallest(root, 3)

    print(ans)


