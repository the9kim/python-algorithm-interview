from typing import List

def solution(numbers: List[int]):

    results = []

    for n in numbers:
        bin_num = bin(n)[2:]

        node_nums = find_node_count(bin_num)

        binary_tree = pad_binary_tree(bin_num, node_nums)

        if is_representable(binary_tree, 0, len(binary_tree) - 1, True):
            results.append(1)
        else:
            results.append(0)

    return results

def find_node_count(bin: str) -> int:
    node_count = 0
    level = 0

    while len(bin) > node_count:
        node_count += 2 ** level
        level += 1

    return node_count

def pad_binary_tree(bin: str, node_nums: int) -> str:
    padding_size = node_nums - len(bin)
    padding = "0" * padding_size

    return padding + bin


def is_representable(binary_tree: str, left: int, right: int, has_parent: bool) -> bool:

    if left > right:
        return True

    mid = left + (right - left) // 2

    if not has_parent and binary_tree[mid] == '1':
        return False

    has_parent = binary_tree[mid] == '1'

    return (is_representable(binary_tree, left, mid - 1, has_parent)
            and is_representable(binary_tree, mid + 1, right, has_parent))
