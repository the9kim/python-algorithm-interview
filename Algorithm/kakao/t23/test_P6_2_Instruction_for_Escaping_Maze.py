from unittest import TestCase

from Algorithm.kakao.t23 import P6_2_Instruction_for_Escaping_Maze


class Test(TestCase):
    def setUp(self):
        self.p6 = P6_2_Instruction_for_Escaping_Maze

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
