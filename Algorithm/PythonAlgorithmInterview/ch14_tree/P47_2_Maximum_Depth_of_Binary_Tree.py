from typing import Optional
import collections


class P47_2_Maximum_Depth_of_Binary_Tree:
    class TreeNode:
        def __init__(self, val: int = 0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    # Using Iterative BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = collections.deque([root])
        depth = 0

        while q:
            q_size = len(q)
            depth += 1

            for i in range(q_size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return depth
