class P22_1_Daily_Temperatures:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)

        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < temp:

                top = stack.pop()
                answer[top] = i - top

            stack.append(i)

        return answer



if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    p22 = P22_1_Daily_Temperatures()
    answer = p22.dailyTemperatures(temperatures)

    print(answer)