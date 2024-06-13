class P2_1_Bracket_Transformation:
    '''
    1. Split the input into the balanced bracket 'W' which can't be split anymore and the rest part named 'U'
    2. Keep splitting the rest part 'U' using recursion
    3. Check if 'W' is valid or not and Combine 'U'
    '''

    def solution(self, p: str) -> str:
        if p == "":
            return ""

        # 1.
        idx = self.split_bracket(p)
        left = p[0: idx]
        # 2.
        right = self.solution(p[idx:])

        if self.isValid(left):
            return left + right
        else:
            return '(' + right + ')' + self.replace(left[1 : -1])

    def split_bracket(self, p: str) -> int:
        open = 0
        close = 0

        for s in p:
            if s == '(':
                open += 1
            else:
                close += 1

            if open == close:
                return open + close

    def isValid(self, left: int) -> bool:
        stack = []

        for e in left:
            if e == '(':
                stack.append(e)
            else:
                if not stack:
                    return False
                stack.pop()
        if stack:
            return False

        return True

    def replace(self, p: str) -> str:
        replaced = ""

        for e in p:
            if e == '(':
                replaced += ')'
            else:
                replaced += '('

        return replaced
