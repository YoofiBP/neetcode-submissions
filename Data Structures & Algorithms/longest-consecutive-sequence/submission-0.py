class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        current = []
        windows = []

        nums.sort()

        for i in range(len(nums)):
            if len(current) == 0:
                current.append(nums[i])
            elif nums[i] - current[-1] == 1:
                current.append(nums[i])
            elif nums[i] - current[-1] > 1:
                windows.append((len(current), current))
                current = [nums[i]]
        windows.append((len(current), current))

        windows.sort(key= lambda x:x[0])

        answer = windows[-1][0]

        return answer