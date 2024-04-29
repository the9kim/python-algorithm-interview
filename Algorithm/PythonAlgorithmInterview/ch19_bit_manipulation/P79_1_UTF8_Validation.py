from typing import List


class P79_1_UTF8_Validation:
    def validUtf8(self, data:List[int]) -> bool:
        start = 0
        def check_rest_bytes(size: int) -> bool:
            for i in range(start + 1, start + 1 + size):
                if i >= len(data) or data[i] >> 6 != 0b10:
                    return False
            return True

        while start < len(data):
            if data[start] >> 3 == 0b11110 and check_rest_bytes(3):
                start += 4
            elif data[start] >> 4 == 0b1110 and check_rest_bytes(2):
                start += 3
            elif data[start] >> 5 == 0b110 and check_rest_bytes(1):
                start += 2
            elif data[start] >> 7 == 0b0:
                start += 1
            else:
                return False

        return True


