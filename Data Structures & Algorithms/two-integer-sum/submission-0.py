class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # i != j
        # return [i,j] , nums[i] + nums[j] == target

        # a + b = target
        # target - a = b
        seen = {}
        for i, a in enumerate(nums):
            b = target - a
            if b in seen:
                return [seen[b], i]

            seen[a] = i
        
        