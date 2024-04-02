from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class P59_1_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        in_idx = inorder.index(preorder[0])

        node = TreeNode(inorder[in_idx])

        node.left = self.buildTree(preorder[1: 1 + in_idx], inorder[0:in_idx])
        node.right = self.buildTree(preorder[1 + in_idx:], inorder[in_idx + 1:])

        return node
