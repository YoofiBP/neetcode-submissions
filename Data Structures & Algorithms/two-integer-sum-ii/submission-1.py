class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        p1 = 0

        difference = target - numbers[p1]

        while True:
            foundIndex = self.binarySearch(numbers, p1 + 1, difference)
            if foundIndex != -1:
                return [p1+1, foundIndex +1]
            else:
                p1 += 1
                difference = target - numbers[p1]
                
    def binarySearch(self, arr, start, target):
            end = len(arr)-1
    
            while start <= end:
                middle = start + ((end - start) // 2)
    
                if arr[middle] > target:
                    end = middle - 1
                elif arr[middle] < target:
                    start = middle + 1
                else:
                    return middle
            return -1