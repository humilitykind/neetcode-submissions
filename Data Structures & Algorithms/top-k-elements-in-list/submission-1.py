class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        
        # 2. Bucket: index = frequency, value = list of numbers with that frequency
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            freq_buckets[count].append(num)
            
        # 3. Gather top k from highest frequency bucket down to lowest
        res = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res