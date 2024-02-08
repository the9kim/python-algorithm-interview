class P7_1_Two_Sum:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]


    def twoSum2(self, nums:list[int], target:int) -> list[int]:
        indexDict = {}

        for i, num in enumerate(nums):
            indexDict[num] = i

        for i, num in enumerate(nums):
            subtraction = target - num
            if subtraction in indexDict and i != indexDict[subtraction]:
                return [i, indexDict[subtraction]]

    def twoSum3(self, nums:list[int], target:int) -> list[int]:
        indexDict = {}

        for i, num in enumerate(nums):
            subtraction = target - num
            if subtraction in indexDict and i != indexDict[subtraction]:
                return [i, indexDict[subtraction]]

            indexDict[num] = i







