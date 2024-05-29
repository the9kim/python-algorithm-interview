from unittest import TestCase

from Algorithm.kakao.t18.P1_1_Dart_Game import P1_1_Dart_Game

class TestP1_1_Dart_Game(TestCase):

    def setUp(self):
        self.p1 = P1_1_Dart_Game()
    def test_solution(self):
        dart_result = "1D#2S*3S"
        expected = 5

        answer = self.p1.solution(dart_result)

        self.assertEqual(expected, answer)



