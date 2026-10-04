class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = defaultdict(int)

        for i in s1:
            s1Count[i] += 1

        p1 = 0
        p2 = 0

        subCount = defaultdict(int)

        for p2 in range(len(s2)):
            if s2[p2] not in s1Count:
                p1 = p2 + 1
                subCount = defaultdict(int)
            else:
                subCount[s2[p2]] += 1


                while subCount[s2[p2]] > s1Count[s2[p2]]:
                    subCount[s2[p1]] -= 1
                    p1 += 1
                    
                if p2 - p1 + 1 == len(s1):
                    return True

        return False