import collections
from typing import List

class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        crnt = self.root

        for w in word:
            crnt.count += 1
            crnt = crnt.children[w]
        crnt.count += 1

    def search(self, word: str) -> int:
        crnt = self.root
        for w in word:
            if w == '?':
                return crnt.count
            if w not in crnt.children:
                return 0
            crnt = crnt.children[w]

class P4_1_Searching_Lyrics:
    '''
    1. Create Tries and reversed-Tires based on length of words
    2. Insert words and into each Trie
    3. Search Tries using queries depending on the position of '?' query
    '''
    def solution(self, words: str, queries: str) -> List[int]:
        # 1.
        tries = collections.defaultdict(Trie)
        re_tries = collections.defaultdict(Trie)

        # 2.
        for word in words:
            tries[len(word) - 1].insert(word)
            re_tries[len(word) - 1].insert(word[::-1])

        # 3
        answer = []
        for query in queries:
            if query.endswith('?'):
                answer.append(tries[len(query) - 1].search(query))
            elif query.startswith('?'):
                answer.append(re_tries[len(query) - 1].search(query[::-1]))

        return answer








