from typing import List
import collections


class P36_1_Letter_Combination_of_a_Phone_Number:
    def dfs(self, graph: dict[str, List], digits: str, answer: List[str], index: int, string_builder: str):
        if len(string_builder) == len(digits):
            answer.append(string_builder)
            return

        for s in graph[digits[index]]:
            new_str_builder = string_builder + s
            self.dfs(graph, digits, answer, index + 1, new_str_builder)


    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        graph = collections.defaultdict(list)
        graph["2"] = ["a", "b", "c"]
        graph["3"] = ["d", "e", "f"]
        graph["4"] = ["g", "h", "i"]
        graph["5"] =  ["j", "k", "l"]
        graph["6"] =  ["m", "n", "o"]
        graph["7"] =  ["p", "q", "r", "s"]
        graph["8"] =  ["t", "u", "v"]
        graph["9"] =  ["w", "x", "y", "z"]

        answer = list()

        self.dfs(graph, digits, answer, 0, "")

        return answer
