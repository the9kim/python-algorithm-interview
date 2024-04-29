from unittest import TestCase

from Algorithm.PythonAlgorithmInterview.ch19_bit_manipulation.P78_1_Sum_of_Two_Integers import P78_1_Sum_of_Two_Integer


class TestP78_1_Sum_of_Two_Integer(TestCase):

    def setUp(self):
        self.p78 = P78_1_Sum_of_Two_Integer()
    def test_get_sum(self):
        a = 1
        b = 2
        expected = 3

        answer = self.p78.getSum(a, b)

        self.assertEqual(expected, answer)
