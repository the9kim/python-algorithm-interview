import collections

class P8_3_Trapping_Rain_water:
    def trap(self, height:list[int])-> int:

        volume = 0

        stack = collections.deque()

        for i in range(len(height)):

            while (len(stack) != 0 and height[stack[-1]] < height[i]):
                floor = stack.pop()

                if len(stack) == 0:
                    break

                # Calculate the length of the volume
                L = i - stack[-1] - 1

                # Calculate the height of the volume
                H = min(height[stack[-1]], height[i]) - height[floor]

                # Calculate the Volume
                volume += L * H


            stack.append(i)

        return volume

if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    p8 = P8_3_Trapping_Rain_water()
    volume = p8.trap(height)
    print(volume)