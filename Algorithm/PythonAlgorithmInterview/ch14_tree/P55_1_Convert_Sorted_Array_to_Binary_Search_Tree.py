from typing import List, Optional

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
class P55_1_Convert_Sorted_Array_to_Binary_Search_Tree:
    def sortedArrayToBST(self, nums:List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        def dfs(left: int, right: int) -> TreeNode:

            if left > right:
                return None

            mid = left + (right - left) // 2

            root = TreeNode(nums[mid])

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root


        return dfs(0, len(nums) - 1)




