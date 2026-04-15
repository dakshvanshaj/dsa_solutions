class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # counter -> k,v -> (nums[i], count(nums[i]))
        counter = {}

        for i in range(n):
            counter[nums[i]] = counter.get(nums[i], 0) + 1
        
        counter_sorted = dict(sorted(counter.items(), key=(lambda item: item[1])))

        return list(counter_sorted.keys())[-k:]