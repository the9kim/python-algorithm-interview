import collections
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = int
        self.left = left
        self.right = right


class P52_1_Serialize_and_Deserialize_Binary_Tree:
    def serialize(self, root: TreeNode) -> str:
        if root is None:
            return "#"

        q = collections.deque([root])
        q.append(root)

        result = ["#"]
        result.append(str(root.val))

        while q:
            node = q.popleft()

            if node.left:
                q.append(node.left)
                result.append(str(node.left.val))
            else:
                result.append("#")

            if node.right:
                q.append(node.right)
                result.append(str(node.right.val))
            else:
                result.append("#")

        return ','.join(result)

    def deserialize(self, data: str) -> TreeNode:
        if data == "#":
            return None

        tree_arr = data.split(',')

        root = TreeNode(int(tree_arr[1]))

        q = collections.deque([root])
        q.append(root)

        index = 2

        while q:
            node = q.popleft()

            if tree_arr[index] != "#":
                node.left = TreeNode(int(tree_arr[index]))
                q.append(node.left)

            index += 1

            if tree_arr[index] != "#":
                node.right = TreeNode(int(tree_arr[index]))
                q.append(node.right)

            index += 1


        return root


