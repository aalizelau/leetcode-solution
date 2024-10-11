def jump(nums):
    n = len(nums)
    jumps = 0
    max_reachable = 0
    current_jump_end = 0
    
    for i in range(n - 1): 
        max_reachable = max(max_reachable, i + nums[i])
        
        # If we have reached the end of the current jump range
        if i == current_jump_end:
            jumps += 1
            current_jump_end = max_reachable
            
            # If we can reach or pass the last index, we are done
            if current_jump_end >= n - 1:
                break
    
    return jumps