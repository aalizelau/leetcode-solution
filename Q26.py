def removeDuplicates(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.pop(i + 1)  # Remove duplicate
        else:
            i += 1  # Move to the next element if it's unique
    return len(nums)