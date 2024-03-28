from typing import Optional
import collections


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class P57_3_Range_Sum_of_BST:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0

        stack = collections.deque()

        stack.append(root)

        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                sum += node.val

            if node.val > low and node.left is not None:
                stack.append(node.left)

            if node.val < high and node.right is not None:
                stack.append(node.right)

        return sum








