from unittest import TestCase

from Algorithm.kakao.t23.P3_1_Emoji_Discount_Promotion import P3_1_Emoji_Discount_Promotion


class TestP3_1_Emoji_Discount_Promotion(TestCase):
    def setUp(self):
        self.p3 = P3_1_Emoji_Discount_Promotion()

    def test_solution(self):
        users = [[40, 10000], [25, 10000]]
        emoticons = [7000, 9000]
        expected = [1, 5400]

        answer = self.p3.solution(users, emoticons)

        self.assertEqual(expected, answer)
