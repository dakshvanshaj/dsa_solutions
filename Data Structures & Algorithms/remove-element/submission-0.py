class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # iterate over nums
        # two pointers -> nums[0], iterate until we find num[i] != 0
        # if pointer1 = val: replace with pointer2 value
        # then count 

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
                
        return k

        
