from typing import List

class P2_1_Parcel_Delivery_and_Pickup:

    '''
    1. Utilize iteration in reversed order and Find the index whose value is not zero and update the distance
    2. Remove the elements up to the amount of the capacity size
    '''
    def solution(self, cap: int, n: int, deliveries: List[int], pickups: List[int]) -> int:
        d_idx = n
        p_idx = n

        distance = 0

        while d_idx > 0 or p_idx > 0:
            while d_idx > 0 and deliveries[d_idx - 1] == 0:
                d_idx -= 1

            while p_idx > 0 and pickups[p_idx - 1] == 0:
                p_idx -= 1

            distance += max(d_idx, p_idx) * 2

            d_idx = self.update_position(d_idx, deliveries, cap)
            p_idx = self.update_position(p_idx, pickups, cap)

        return distance

    def update_position(self, index: int, parcels: List[int], capa: int) -> int:
        while index > 0:
            if parcels[index - 1] > capa:
                parcels[index - 1] -= capa
                break
            else:
                capa -= parcels[index - 1]
                parcels[index - 1] = 0
                index -= 1

        return index

