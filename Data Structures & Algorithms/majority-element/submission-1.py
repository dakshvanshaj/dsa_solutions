class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        mj_len = n/2
        # nums[i] -> majority elem if  count(nums[i]) > mj_len 

        counter = {}

        for i in range(n):
            counter[nums[i]] = counter.get(nums[i], 0) + 1
        
        for k, v in counter.items():
            if v > mj_len:
                return k