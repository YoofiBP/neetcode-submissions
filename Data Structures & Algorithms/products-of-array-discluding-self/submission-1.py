class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [0 for x in nums]

        running_prefix = 0
        running_suffix = 0

        for i in range(len(result)):
            running_prefix = 1 if i == 0 else running_prefix * nums[i-1]
            result[i] = running_prefix


        for i in range(-1, -(len(nums) + 1), -1):
            running_suffix = 1 if i == -1 else running_suffix * nums[i+1]
            result[i] = result[i] * running_suffix

        return result