class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHeight = 0
        # area is min height x index diff

        p1 = 0
        p2 = len(heights) - 1

        while p1 < p2:
            start = heights[p1]
            end = heights[p2]

            height = min(start, end)
            width = p2 - p1

            maxHeight = max(maxHeight, height * width)

            if start < end:
                p1 += 1
            else:
                p2 -= 1

        return maxHeight