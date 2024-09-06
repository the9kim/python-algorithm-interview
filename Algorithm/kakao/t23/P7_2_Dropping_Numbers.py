from collections import deque
from typing import List


class TreeNode:
    def __init__(self, idx: int, target: int):
        self.idx = idx
        self.target = target
        self.card_cnt = 0
        self.has_valid_cards = False
        self.children = deque()


def solution(edges: List[List[int]], target: List[int]) -> List[int]:
    root = create_sorted_tree(edges, target)

    leaf_sequence = retrieve_leaf_cards_cnt(root, sum(1 for n in target if n != 0))
    if leaf_sequence is None:
        return [-1]

    dropped_leaves = determine_card_values(leaf_sequence)

    return dropped_leaves


def create_sorted_tree(edges: List[List[int]], target: List[int]) -> TreeNode:
    nodes = [TreeNode(i, t) for i, t in enumerate(target)]

    for src, dst in edges:
        nodes[src - 1].children.append(nodes[dst - 1])

    for node in nodes:
        node.children = deque(sorted(node.children, key=lambda x: x.idx))

    return nodes[0]


def retrieve_leaf_cards_cnt(root: TreeNode, place_holder: int) -> List[TreeNode]:
    leaf_sequence = []

    while place_holder > 0:
        node = root

        while node.children:
            next = node.children.popleft()
            node.children.append(next)
            node = next

        node.card_cnt += 1
        leaf_sequence.append(node)

        if node.card_cnt > node.target:
            return None

        if not node.has_valid_cards and node.card_cnt * 3 >= node.target:
            node.has_valid_cards = True
            place_holder -= 1

    return leaf_sequence

def determine_card_values(leaf_sequence: List[TreeNode]) -> List[int]:
    dropped_cards = []

    for leaf in leaf_sequence:
        leaf.card_cnt -= 1
        for card_val in range(1, 4):
            if leaf.card_cnt * 3 >= leaf.target - card_val:
                leaf.target -= card_val
                dropped_cards.append(card_val)
                break

    return dropped_cards


