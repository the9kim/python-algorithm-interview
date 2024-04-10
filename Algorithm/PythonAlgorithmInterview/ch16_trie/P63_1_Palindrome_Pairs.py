from typing import List
import collections

class TrieNode:
    def __init__(self):
        self.index = -1
        self.children = collections.defaultdict(TrieNode)
        self.palindrome = list()
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def is_palindrome(self, left:int, right:int, word:str) -> bool:
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    def insert(self, index: int, word: str) -> None:

        node = self.root

        for i in range(len(word) - 1, -1, -1):
            if self.is_palindrome(0, i, word):
                node.palindrome.append(index)

            node = node.children[word[i]]

        node.index = index

    def search(self, index: int, word: str) -> List[List[int]]:
        answer = list()
        node = self.root

        for i in range(0, len(word)):
            if node.index != -1 and self.is_palindrome(i, len(word) - 1, word):
                answer.append([index, node.index])

            if word[i] not in node.children:
                return answer

            node = node.children[word[i]]

        if node.index != -1 and node.index != index:
            answer.append([node.index, index])

        for p in node.palindrome:
            answer.append([index, p])

        return answer

class P63_1_Palindrome_Pairs:

    def palindromePairs(self, words:List[str]) -> List[List[str]]:
        trie = Trie()
        answer = []

        for i, word in enumerate(words):
            trie.insert(i, word)

        for i, word in enumerate(words):
            answer += trie.search(i, word)

        return answer


if __name__ == '__main__':
    words = ["abcd","dcba","lls","s","sssll"]

    p63 = P63_1_Palindrome_Pairs()
    answer = p63.palindromePairs(words)

    print(answer)
