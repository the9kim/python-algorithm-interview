class P8_2_Trapping_Rain_Water:
    def trap(self, height: list[int]) -> int:

        volume = 0

        left = 0
        left_H = 0

        right = len(height) - 1
        right_H = 0

        while left < right:
            left_H = max(left_H, height[left])
            right_H = max(right_H, height[right])

            if left_H <= right_H:
                volume += left_H - height[left]
                left += 1
            else:
                volume += right_H - height[right]
                right -= 1

        return volume

if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    p8 = P8_2_Trapping_Rain_Water()
    volume = p8.trap(height)
    print(volume)