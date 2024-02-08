class P20_1_Valid_Parentheses:
    def isValid(self, s: str) -> bool:

        table = {')': '(', ']': '[', '}': '{'}

        stack = []

        for p in s:
            if p not in table:
                stack.append(p)

            else:
                if not stack or table[p] != stack.pop():
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    s = "()[]{}"
    p20 = P20_1_Valid_Parentheses()
    is_valid = p20.isValid(s)

    print(is_valid)
