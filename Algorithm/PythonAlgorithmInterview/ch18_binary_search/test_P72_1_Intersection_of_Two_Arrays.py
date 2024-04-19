from unittest import TestCase

from Algorithm.PythonAlgorithmInterview.ch18_binary_search.P72_1_Intersection_of_Two_Arrays import \
    P72_1_Intersection_of_Two_Arrays


class TestP72_1_Intersection_of_Two_Arrays(TestCase):

    def setUp(self):
        self.p72 = P72_1_Intersection_of_Two_Arrays()

    def test_intersection(self):
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        expected = [4, 9]

        intersection = self.p72.intersection(nums1, nums2)

        self.assertEqual(intersection, expected)
