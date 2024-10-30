from typing import List

def solution(cap: int, n :int, deliveries: List[int], pickups: List[int]) -> int:

    dIdx = n
    pIdx = n

    distance = 0

    while dIdx > 0  or pIdx > 0:
        dIdx = getToFurthestHouse(dIdx, deliveries)
        pIdx = getToFurthestHouse(pIdx, pickups)

        distance += max(dIdx, pIdx) * 2

        dIdx = deliver_or_pickup(dIdx, deliveries, cap)
        pIdx = deliver_or_pickup(pIdx, pickups, cap)

    return distance

def getToFurthestHouse(idx: int, parcels: List[int]) -> int:

    while idx > 0 and  parcels[idx - 1] == 0:
        idx -= 1

    return idx

def deliver_or_pickup(idx: int, parcels: List[int], cap: int) -> int:
    while idx > 0:
        if cap < parcels[idx - 1]:
            parcels[idx - 1] -= cap
            break
        else:
            cap -= parcels[idx - 1]
            parcels[idx - 1] = 0
            idx -= 1

    return idx
