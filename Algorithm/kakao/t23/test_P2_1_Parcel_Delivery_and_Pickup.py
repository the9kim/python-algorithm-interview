from unittest import TestCase

from Algorithm.kakao.t23.P2_1_Parcel_Delivery_and_Pickup import P2_1_Parcel_Delivery_and_Pickup


class TestP2_1_Parcel_Delivery_and_Pickup(TestCase):

    def setUp(self):
        self.p2 = P2_1_Parcel_Delivery_and_Pickup()

    def test_solution(self):
        cap = 4
        n = 5
        deliveries = [1, 0, 3, 1, 2]
        pickups = [0, 3, 0, 4, 0]

        expected = 16

        answer = self.p2.solution(cap, n, deliveries, pickups)

        self.assertEqual(expected, answer)