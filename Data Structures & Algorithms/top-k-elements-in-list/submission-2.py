class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []

        counts = defaultdict(int)

        for i in nums:
            counts[i] += 1

        for key in counts.keys():
            if(len(heap) == k):
                if counts[key] > heap[0][0]:
                    heapq.heapreplace(heap, (counts[key], key))
            else:
                heapq.heappush(heap, (counts[key], key))

        return [x[1] for x in heap]