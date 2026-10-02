class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        for i , n in enumerate(nums):
            counts[n] = 1 +counts.get(n,0)

        sorted_keys = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
        return sorted_keys[:k]

            

        