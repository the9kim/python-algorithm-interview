class P1_2_Reverse_String:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1;

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseString2(self, s: list[str]) -> None:
        s.reverse()

if __name__ == '__main__':

    s = ["h", "e", "l", "l", "o"]
    rs = P1_2_Reverse_String()
    rs.reverseString2(s)
    print(s)
