class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class P56_1_Binary_Search_Tree_to_Greater_Sum_Tree:

    sum = 0
    def bstToGst(self, root:TreeNode) -> TreeNode:

        if root.right:
            self.bstToGst(root.right)

        self.sum += root.val
        root.val = self.sum

        if root.left:
            self.bstToGst(root.left)

        return root