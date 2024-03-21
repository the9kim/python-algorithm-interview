class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class P53_1_Balanced_Binary_Tree:
    def isBalanced(self, root: TreeNode) -> bool:

        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        if dfs(root) == -1:
            return False

        return True

