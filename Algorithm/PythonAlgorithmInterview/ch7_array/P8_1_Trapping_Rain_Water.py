class P8_1_Trapping_Rain_Water:
    def trap(self, height: list[int]) -> int:
        amount = 0
        left = 0

        while left < len(height) - 1:
            if height[left] > 0:

                right = left + 1
                maxIndex = 0
                maxHeight = 0

                while right < len(height):
                    if height[left] <= height[right]:
                        amount += self.calculateWaterAmount(left, right, height)
                        left = right - 1
                        break

                    if height[right] >= maxHeight:
                        maxIndex = right
                        maxHeight = height[right]

                    if right == len(height) - 1:
                        amount += self.calculateWaterAmount(left, maxIndex, height)
                        left = maxIndex - 1

                    right += 1

            left += 1

        return amount

    def calculateWaterAmount(self, left:int, right:int, height:list[int])-> int:
        waterAmount = 0
        minHeight = min(height[left], height[right])

        for i in range(left + 1, right):
            waterAmount += minHeight - height[i]

        return waterAmount

