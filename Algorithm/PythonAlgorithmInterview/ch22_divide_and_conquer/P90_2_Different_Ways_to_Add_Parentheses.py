from typing import List


class P90_2_Different_Ways_to_Add_Parentheses:

    # The book solution
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left: List[int], right: List[int], op: str) -> List[int]:
            result = []
            for l in left:
                for r in right:
                    result.append(eval(str(l) + op + str(r)))
            return result

        results = []

        if expression.isdigit():
            results.append(int(expression))

        for i, n in enumerate(expression):
            if n in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                results.extend(compute(left, right, n))

        return results