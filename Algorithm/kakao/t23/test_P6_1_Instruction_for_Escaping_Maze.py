from unittest import TestCase

from Algorithm.kakao.t23.P6_1_Instruction_for_Escaping_Maze import P6_1_Instruction_for_Escaping_Maze


class TestP6_1_Instruction_for_Escaping_Maze(TestCase):
    def setUp(self):
        self.p6 = P6_1_Instruction_for_Escaping_Maze()

    def test_solution(self):
        n = 3
        m = 4
        x = 2
        y = 3
        r = 3
        c = 1
        k = 5
        expected = "dllrl"

        answer = self.p6.solution(n, m, x, y, r, c, k)

        self.assertEquals(expected, answer)
