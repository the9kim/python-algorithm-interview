from unittest import TestCase

from Algorithm.PythonAlgorithmInterview.ch17_sort.P67_1_Largest_Number import P67_1_Largest_Number


class TestP67_1_Largest_Number(TestCase):

    def setUp(self):
        self.p67 = P67_1_Largest_Number()
    def test_largest_number(self):
        nums = [3, 30, 34, 5, 9]
        expected = "9534330"

        answer = self.p67.largestNumber(nums)

        self.assertEqual(answer, expected)
