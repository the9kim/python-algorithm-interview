class ProductOfArrayExceptSelf:
    def productExceptSelf(self, nums:list[int]) -> list[int]:

        answer = [1] * len(nums)

        product = 1

        # 1. Calculate the left-side product of the array
        for i in range(len(nums)):
            answer[i] = product
            product *= nums[i]

        # 2. Calculate the right-side product of the array
        product = 1

        for j in range(len(nums) - 1, -1, -1):
            answer[j] *= product
            product *= nums[j]

        return answer
