class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} # num : frequency of num
        bucket = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
            
        for n, c in hashmap.items():
            bucket[c].append(n)
            
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for b in bucket[i]:
                res.append(b)
                if len(res) == k:
                    return res   