def rearrange(word: str):
    return "".join(sorted(word))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)
        output = []

        for s in strs:
            sorted_s = rearrange(s)
            buckets[sorted_s].append(s)

        for k in buckets:
            output.append(buckets[k])

        return output