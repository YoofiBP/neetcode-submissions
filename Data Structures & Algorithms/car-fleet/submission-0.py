class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        positions = sorted([(position[x], speed[x]) for x in range(len(position))], reverse=True)

        stack = []

        for x in positions:
            if len(stack) < 1:
                stack.append(x)
                continue

            previous = stack[-1]

            previousTimeToComplete = (target - previous[0]) / previous[1]
            currentTimeToComplete = (target - x[0]) / x[1]

            if currentTimeToComplete <= previousTimeToComplete:
                if x[1] < previous[1]:
                    stack.pop()
                    stack.append(x)
            else:
                stack.append(x)

        return len(stack)