from unittest import TestCase

from Algorithm.PythonAlgorithmInterview.ch18_binary_search.P73_1_Two_Sum import P73_1_Two_Sum


class TestP73_1_Two_Sum(TestCase):
    def setUp(self):
        self.p73 = P73_1_Two_Sum()
    def test_two_sum(self):
        # given
        numbers = [-1, 0]
        target = -1
        expected = [1, 2]

        # when
        answer = self.p73.twoSum(numbers, target)
        self.assertEqual(expected, answer)
