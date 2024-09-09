from unittest import TestCase

from Algorithm.kakao.t17.P1_1_Coloring_Book import P1_1_Coloring_Book


class TestP1_1_Coloring_Book(TestCase):

    def setUp(self):
        self.p1 = P1_1_Coloring_Book()
    def test_solution(self):
        m = 6
        n = 4
        picture = [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]
        expected = [4, 5]

        answer = self.p1.solution(m, n, picture)

        self.assertEquals(expected, answer)


