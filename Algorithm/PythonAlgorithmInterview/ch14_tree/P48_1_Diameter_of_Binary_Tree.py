from typing import Optional


class P48_1_Diameter_of_Binary_Tree:
    class TreeNode:
        def __init__(self, val: int = 0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    diameter: int = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[P48_1_Diameter_of_Binary_Tree.TreeNode]) -> int:
            if node is None:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left + right + 2)

            return max(left, right) + 1

        dfs(root)

        return self.diameter




