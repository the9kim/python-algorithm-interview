from unittest import TestCase

from Algorithm.kakao.t21 import P5_2_Advertise_Insertion


class Test(TestCase):

    def setUp(self):
        self.p5 = P5_2_Advertise_Insertion

    def test_solution(self):
        play_time = "02:03:55"
        adv_time = "00:14:15"
        logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
        expected = "01:30:59"

        answer = self.p5.solution(play_time, adv_time, logs)

        self.assertEqual(expected, answer)
