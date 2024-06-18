import re
from typing import List


class P1_1_New_Id_Recommendation:
    def solution(self, new_id: str) -> str:
        new_id = new_id.lower()
        new_id = re.sub("[^a-z0-9-_.]", "", new_id)
        new_id = re.sub("\\.+", ".", new_id)
        if new_id.startswith("."):
            new_id = new_id[1:]
        if new_id.endswith("."):
            new_id = new_id[:-1]
        if new_id == "":
            new_id = "a"
        if len(new_id) > 15:
            new_id = new_id[:15]
            if new_id.endswith("."):
                new_id = new_id[:-1]
        while len(new_id) <= 2:
            new_id += new_id[-1]

        return new_id
