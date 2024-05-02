from unittest import TestCase

from Algorithm.PythonAlgorithmInterview.ch20_sliding_window.P81_1_Sliding_Window_Maximum import \
    P81_Sliding_Window_Maximum


class TestP81_Sliding_Window_Maximum(TestCase):
    def setUp(self):
        self.p81 = P81_Sliding_Window_Maximum()
    def test_max_sliding_window(self):
        # given
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [3,3,5,5,6,7]

        # when
        answer = self.p81.maxSlidingWindow(nums, k)

        # then
        self.assertEqual(expected, answer)
