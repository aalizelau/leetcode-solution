def summary_ranges(nums):
    ranges = []
    if not nums:
        return ranges

    start = nums[0]
    
    for i in range(len(nums) - 1):
        # Check if the next number is not consecutive
        if nums[i] + 1 != nums[i + 1]:
            # If start and nums[i] are the same, it's a single number
            if start == nums[i]:
                ranges.append(f"{start}")
            else:
                ranges.append(f"{start}->{nums[i]}")
            # Update start to the next number
            start = nums[i + 1]
    
    # Add the final range
    if start == nums[-1]:
        ranges.append(f"{start}")
    else:
        ranges.append(f"{start}->{nums[-1]}")

    return ranges