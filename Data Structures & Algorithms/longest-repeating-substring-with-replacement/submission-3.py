class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)

        longest, maxF, p1 = 0, 0, 0

        for p2 in range(len(s)):
            counts[s[p2]] += 1
            maxF = max(counts[s[p2]], maxF)

            while (p2 - p1 + 1) - maxF > k:
                counts[s[p1]] -= 1
                p1 += 1

            longest = max(p2 - p1 + 1, longest)

        return longest