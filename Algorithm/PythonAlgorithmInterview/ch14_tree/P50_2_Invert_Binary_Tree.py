from typing import Optional
import collections


class TreeNode:
    def __init(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
class P50_1_Invert_Binary_Tree:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        q = collections.deque([root])

        while q:
            node = q.popleft()
            if node:
                node.left, node.right = node.right, node.left

                q.append(node.left)
                q.append(node.right)

        return root










