class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        currentMin = float('inf')

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return min(nums[0], nums[1])

        while True:
            middle = ((right - left) // 2) + left
            currentMin = min(currentMin, nums[middle])
            
            if nums[left] < nums[middle] and nums[middle] < nums[right]:
                return min(nums[left], currentMin)
            if nums[left] > nums[middle]:
                right = middle - 1
            else:
                left = middle + 1

            if right - left == 1 or right - left == -1:
                if right < len(nums):
                    currentMin = min([nums[right],currentMin])
                if left < len(nums):
                    currentMin = min([nums[left],currentMin])
                break

        return currentMin