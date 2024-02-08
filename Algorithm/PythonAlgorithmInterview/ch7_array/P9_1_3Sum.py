class P9_1_3Sum:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []

        # the 'sort()' method sorts a list in-place and return None
        nums.sort()

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return answer


if __name__ == '__main__':
    nums2 = [-1, -1, -1, 0, 1, 2, 2]
    nums = [1,-1,-1,0]

    p9 = P9_1_3Sum()

    three_sum = p9.threeSum(nums)

    print(three_sum)
