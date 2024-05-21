from typing import List


class P90_1_Different_Ways_to_Add_Parentheses:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []

        for i, n  in enumerate(expression):
            if n == '+' or n == '-' or n == '*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                for l in left:
                    for r in right:
                        if n == '+':
                            result.append(l + r)
                        elif n == '-':
                            result.append(l - r)
                        elif n == '*':
                            result.append(l * r)

        if not result:
            result.append(int(expression))

        return result




