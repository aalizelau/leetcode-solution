class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        longest_streak = 0

        for num in nums: 
            if num-1 not in nums_set:
                current_streak = 1
                current_num = num 

                while current_num+1 in nums_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(current_streak,longest_streak)
        return longest_streak