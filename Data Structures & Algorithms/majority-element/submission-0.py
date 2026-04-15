class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        mj_len = n/2
        # nums[i] -> majority elem if  count(nums[i]) > mj_len 

        for i in range(n):
            if nums.count(nums[i]) > mj_len:
                return nums[i]