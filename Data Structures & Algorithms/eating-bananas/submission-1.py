class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        smallest, largest = 1, float('-inf')

        smallest_k = float('inf')

        for x in piles:
            if x > largest:
                largest = x

        while smallest <= largest:
            
            k = ((largest - smallest) // 2) + smallest
            numberOfHoursUsed = 0

            for i in piles:
                if k >= i:
                    numberOfHoursUsed += 1
                    continue

                numberOfHoursUsed += (i // k)
                numberOfHoursUsed += 1 if i - (i // k) * k > 0 else 0

            if numberOfHoursUsed > h:
                smallest = k + 1
            else:
                largest = k - 1
                smallest_k = k if k < smallest_k else smallest_k

        return smallest_k