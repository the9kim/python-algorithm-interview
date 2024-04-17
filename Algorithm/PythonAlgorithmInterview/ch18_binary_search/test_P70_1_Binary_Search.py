from unittest import TestCase

from Algorithm.PythonAlgorithmInterview.ch18_binary_search.P70_1_Binary_Search import P70_1_Binary_Search


class TestP70_1_Binary_Search(TestCase):

    def setUp(self):
        self.p70 = P70_1_Binary_Search()
    def test_binary_search(self):

        # given
        nums = [-1, 0, 3, 5, 9, 12, 15]
        target = 9
        expected = 4

        # when
        answer = self.p70.search(nums, target)

        # then
        self.assertEqual(answer, expected)
