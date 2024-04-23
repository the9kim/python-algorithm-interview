from unittest import TestCase

from Algorithm.PythonAlgorithmInterview.ch18_binary_search.P75_1_Immigration import P75_1_Immigration


class TestP75_1_Immigration(TestCase):

    def setUp(self):
        self.p75 = P75_1_Immigration()
    def test_solution(self):
        times = [7, 10]
        n = 6
        expected = 28

        answer = self.p75.solution(n, times)

        self.assertEqual(expected, answer)
