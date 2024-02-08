import re


class P1_1_Valid_palindrome:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]


if __name__ == '__main__':
    s = "racecar"
    P1_1_Valid_palindrome = P1_1_Valid_palindrome()

    print(P1_1_Valid_palindrome.isPalindrome(s))
