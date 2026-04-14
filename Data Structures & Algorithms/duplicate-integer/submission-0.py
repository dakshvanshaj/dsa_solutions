class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # check if duplicates are present
        #  iterate nums: counter{} , if any of counter.values > 1 -> False esle true

        # set -> keeps/contains only unique

        unique = set(nums)
        if len(unique) < len(nums):
            return True
        else:
            return False