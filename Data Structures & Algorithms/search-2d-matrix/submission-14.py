class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found = None

        for i in range(len(matrix)):
            if matrix[i][0] > target:
                found = matrix[i-1]
                break
            elif matrix[i][0] == target:
                return True

        if len(matrix) == 1:
            found = matrix[0]

        if found is None:
            found = matrix[-1]

        left = 0
        right = len(found) - 1

        print(found)

        while left <= right:
            middle = ((right - left) // 2 )+ left
            if found[middle] == target:
                return True
            elif found[middle] > target:
                right = middle - 1
            elif found[middle] < target:
                left = middle + 1

        return False