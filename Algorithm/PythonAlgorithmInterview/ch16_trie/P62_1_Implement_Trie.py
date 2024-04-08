from typing import List


class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26


class P62_1_Implement_Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for w in word:
            if node.children[ord(w) - ord('a')] is None:
                node.children[ord(w) - ord('a')] = TrieNode()

            node = node.children[ord(w)- ord('a')]

        node.isEnd = True


    def search(self, word: str) -> bool:
        node = self.root

        for w in word:
            if node.children[ord(w) - ord('a')] is None:
                return False

            node = node.children[ord(w) - ord('a')]

        return node.isEnd == True


    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for w in prefix:
            if node.children[ord(w) - ord('a')] is None:
                return False
            node = node.children[ord(w) - ord('a')]

        return True

