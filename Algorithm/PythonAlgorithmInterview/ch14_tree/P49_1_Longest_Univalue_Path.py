from typing import Optional


class P49_1_Longest_Univalue_Path:
    class TreeNode:
        def __init__(self, val: int = 0, left: 'TreeNode' = None,
                     right: 'TreeNode' = None):
            self.val = val
            self.left = left
            self.right = right

    path: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def dfs(node: 'TreeNode') -> int:
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.path = max(self.path, left + right)

            return max(left, right)

        dfs(root)

        return self.path

