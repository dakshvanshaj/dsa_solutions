class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # counter -> k,v -> (nums[i], count(nums[i]))
        counter = {}

        for i in range(n):
            counter[nums[i]] = counter.get(nums[i], 0) + 1
        
        freq = [[] for _ in range(len(nums)+1)]

        for num, cnt in counter.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res