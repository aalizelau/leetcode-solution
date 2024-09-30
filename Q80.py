class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)  # If the length is less than or equal to 2, no changes needed
    
        i = 2  # Start filling from the third position since the first two are allowed
        
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]:  # Compare with the element two positions before
                nums[i] = nums[j]       
                i += 1                  
        
        return i  
        