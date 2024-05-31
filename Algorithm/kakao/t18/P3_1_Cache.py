from typing import List
import collections


class Cache:
    def solution(self, cacheSize: int, cities: List[str]) -> int:

        dq = collections.deque(maxlen=cacheSize)

        time = 0

        for city in cities:
            city = city.lower()
            if city in dq:
                time += 1
                dq.remove(city)
                dq.append(city)

            else:
                time += 5
                dq.append(city)

        return time


