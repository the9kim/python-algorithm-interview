from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
class P51_1_Merge_Two_Binary_Trees:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if root1 and root2:
            node = TreeNode(root1.val + root2.val)

            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)

            return node

        # If root1 only exists, it returns root1, and If root2 only exists, it returns and If both don't exist, it returns None
        else:
            return root1 or root2