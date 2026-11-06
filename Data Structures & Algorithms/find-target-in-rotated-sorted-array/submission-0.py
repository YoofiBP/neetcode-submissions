class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        minimum = (float('inf'),None)

        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        if len(nums) == 2:
            if nums[0] == target: 
                return 0
            if nums[1] == target:
                return 1
            return -1

        while True:
            middle = ((right - left) // 2) + left
            minimum = min(minimum, (nums[left], left), (nums[middle], middle), (nums[right], right))

            if right - left == -1 or right == left:
                break

            if nums[left] < nums[middle] and nums[middle] > nums[right]:
                # its right
                left = middle + 1
            else:
                # its left
                right = middle - 1

        
        candidates = []
        minIndex = minimum[1]

        if minimum[0] == target:
            return minIndex

        left = 0
        right = minIndex - 1 if minIndex > 0 else 0

        while True:
            middle = ((right - left) // 2) + left 

            if middle >= 0 and nums[middle] == target:
                return middle

            if right - left == -1 or right == left:
                break

            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        left = minIndex + 1
        right = len(nums) - 1

        while True:
            middle = ((right - left) // 2) + left

            if nums[middle] == target:
                return middle

            if right - left == -1 or right == left:
                break

            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

      

        return -1