from typing import List, Optional
import sys


class TreeNode:
    def __init__(self, idx: int, x: int, y: int):
        self.idx = idx
        self.x = x
        self.y = y
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class P5_1_Path_Finding_Game:
    '''
    1. Sort the input array in ascending order by the y values
    2. Create a binary tree
    3. Find the pre-order and post-order traversal paths

    * The default recursion limit in Python is 1000. It is necessary to set a new recursion limit using the sys.
    '''

    def solution(self, nodeinfo: List[List[int]]) -> List[List[int]]:
        sys.setrecursionlimit(10**6)
        # 1.
        nodes = []
        for i, n in enumerate(nodeinfo):
            nodes.append(TreeNode(i + 1, n[0], n[1]))

        nodes = sorted(nodes, key=lambda node: (-node.y, node.x))

        # 2.
        def insertNode(root: TreeNode, node: TreeNode) -> None:
            if node.x < root.x:
                if not root.left:
                    root.left = node
                    return
                else:
                    insertNode(root.left, node)
            else:
                if not root.right:
                    root.right = node
                    return
                else:
                    insertNode(root.right, node)

        root = nodes[0]

        for i in range(1, len(nodes)):
            insertNode(root, nodes[i])

        # 3.
        def preorder_traversal(root: TreeNode, route: List[int]) -> None:
            if not root:
                return

            route.append(root.idx)
            preorder_traversal(root.left, route)
            preorder_traversal(root.right, route)

        def postorder_traversal(root: TreeNode, route: List[int]) -> None:
            if not root:
                return

            postorder_traversal(root.left, route)
            postorder_traversal(root.right, route)

            route.append(root.idx)

        preorder = []
        preorder_traversal(root, preorder)

        postorder = []
        postorder_traversal(root, postorder)

        return [preorder, postorder]
