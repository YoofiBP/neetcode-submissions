class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0 for x in temperatures]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temperature, index = stack.pop()
                output[index] = i - index
            stack.append((t, i))

        return output