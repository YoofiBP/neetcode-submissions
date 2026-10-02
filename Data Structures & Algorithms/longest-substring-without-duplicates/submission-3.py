class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = defaultdict(int)

        longest = 0

        p1 = 0
        p2 = 0

        while p2 < len(s):
            if found[s[p2]] > 0:
                longest = max(p2 - p1, longest)
                while found[s[p2]] > 0:
                    found[s[p1]] -= 1
                    p1 += 1
            else:
                found[s[p2]] += 1
                p2 += 1

        longest = max(p2 - p1, longest)        
        return longest