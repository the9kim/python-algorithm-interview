import sys
from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, n: int, y: int, x: int):
        self.n = n
        self.y = y
        self.x = x
        self.left = None
        self.right = None


def solution(nodeinfo: List[List[int]]):
    sys.setrecursionlimit(3000)

    nodes_sorted_in_level = preprocess_data(nodeinfo)

    root = build_tree_node(nodes_sorted_in_level[0][0], nodes_sorted_in_level, 1, -1, 100001)

    preorder = preorder_traversal(root, [])
    postorder = postorder_traversal(root, [])

    return [preorder, postorder]


def preprocess_data(node_info: List[List[int]]) -> List[List[int]]:
    children_dict = defaultdict(list)

    for i, n in enumerate(node_info):
        children_dict[n[1]].append(TreeNode(i + 1, n[1], n[0]))

    return [sorted(nodes, key=lambda node: node.x)
            for _, nodes in sorted(children_dict.items(), key=lambda item: -item[0])]


def build_tree_node(node: TreeNode, nodes: List[List[TreeNode]], idx: int, min_x: int, max_x: int) -> TreeNode:
    if idx >= len(nodes):
        return node

    children_candidates = nodes[idx]

    for child in children_candidates:
        if min_x < child.x < node.x:
            node.left = build_tree_node(child, nodes, idx + 1, min_x, node.x)
        elif node.x < child.x < max_x:
            node.right = build_tree_node(child, nodes, idx + 1, node.x, max_x)

    return node


def preorder_traversal(node: TreeNode, path: List[int]) -> List[int]:
    if not node:
        return path

    path.append(node.n)
    preorder_traversal(node.left, path)
    preorder_traversal(node.right, path)

    return path


def postorder_traversal(node: TreeNode, path: List[int]) -> List[int]:
    if not node:
        return path

    postorder_traversal(node.left, path)
    postorder_traversal(node.right, path)
    path.append(node.n)

    return path
