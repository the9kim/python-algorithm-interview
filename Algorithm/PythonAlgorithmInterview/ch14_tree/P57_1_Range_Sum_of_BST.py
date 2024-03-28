from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class P57_1_Range_Sum_of_BST:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if root is None:
            return 0

        sum = 0

        if root.val >= low and root.val <= high:
            sum += root.val

        sum += self.rangeSumBST(root.left, low, high)
        sum += self.rangeSumBST(root.right, low, high)

        return sum


