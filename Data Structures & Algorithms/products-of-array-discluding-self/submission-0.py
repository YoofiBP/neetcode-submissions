class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix, suffix, result = [[0 for x in nums] for x in range(3)]
        prefix[0] = 1
        suffix[len(nums)-1] = 1

        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]

        for i in range(len(nums)-2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i+1]

        for i in range(len(result)):
            result[i] = prefix[i] * suffix[i]

        return result