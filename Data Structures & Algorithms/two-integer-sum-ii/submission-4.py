class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        p1 = 0
        p2 = len(numbers) - 1

        foundSum = numbers[p1] + numbers[p2]

        while True:
            if foundSum == target:
                break
            elif foundSum > target or p2 == len(numbers)-1:
                p2 -= 1
            else:
                p1 += 1
            foundSum = numbers[p1] + numbers[p2]

        return sorted([p1+1, p2+1])