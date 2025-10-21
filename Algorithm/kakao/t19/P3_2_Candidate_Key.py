from typing import List
import collections
from functools import cmp_to_key

class P3_2_Candidate_Key:

    def solution(self, relation):

        col_size = len(relation[0])
        candidate_keys = []

        for subset in range(1, (1 << col_size)):
            if not self._is_minimal(candidate_keys, subset):
                continue

            if self._is_unique(relation, subset):
                candidate_keys.append(subset)

        return len(candidate_keys)

    def _is_minimal(self, candidate_keys, subset):
        for key in candidate_keys:
            if (subset & key) == key:
                return False

        return True

    def _is_unique(self, relation, subset):
        seen = set()

        selected_cols = [i for i in range(len(relation[0])) if ((1 << i) & subset) != 0]

        for row in relation:
            key_tuple = tuple(row[i] for i in selected_cols)

            if key_tuple in seen:
                return False
            seen.add(key_tuple)

        return True




