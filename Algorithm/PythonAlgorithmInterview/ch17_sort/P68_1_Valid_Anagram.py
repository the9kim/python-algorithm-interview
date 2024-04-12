import unittest

class P68_1_Valid_Anagram:

    def sort_str(self, s: str) -> str:
        return ''.join(sorted(s))
    def isAnagram(self, s: str, t: str) -> bool:
        return self.sort_str(s) == self.sort_str(t)

