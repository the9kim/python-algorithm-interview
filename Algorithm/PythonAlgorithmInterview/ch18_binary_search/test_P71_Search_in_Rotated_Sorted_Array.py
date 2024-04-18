from unittest import TestCase

from Algorithm.PythonAlgorithmInterview.ch18_binary_search.P71_Search_in_Rotated_Sorted_Array import \
    P71_Search_in_Rotated_Sorted_Array


class TestP71_Search_in_Rotated_Sorted_Array(TestCase):
    def setUp(self):
        self.p71 = P71_Search_in_Rotated_Sorted_Array()

    def test_search(self):
        # given
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        expected = 4

        # when
        answer = self.p71.search(nums, target)

        self.assertEqual(answer, expected)

    def test_search2(self):
        # given
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        expected = -1

        # when
        answer = self.p71.search(nums, target)

        self.assertEqual(answer, expected)




