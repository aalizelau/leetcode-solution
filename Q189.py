def rotate(nums, k):
    n = len(nums)
    k = k % n 
    newNums = [] 

    for i in range(n):
        newNums.append(nums[(i - k) % n])
        
    nums[:] = newNums