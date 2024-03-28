from typing import Optional
import collections


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class P57_4_Range_Sum_of_BST:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        sum, q = 0, collections.deque()
        q.append(root)

        while q:
            node = q.popleft()

            if node:
                if low <= node.val <= high:
                    sum += node.val

                if node.val > low:
                    q.append(node.left)

                if node.val < high:
                    q.append(node.right)

        return sum