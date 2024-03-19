from typing import Optional


class P47_1_Maximum_Depth_of_Binary_Tree:
    class TreeNode:
        def __init__(self, val: int = 0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    # Using recursive DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1
