def climbStairs(n):
    # Handle corner cases for n < 3
    if n == 1:
        return 1
    elif n == 2:
        return 2
        
		# a = ways at (n-2), b = ways at (n-1)
    a, b = 2, 1

    for _ in range(n - 2):
        tmp = a
        a = a + b
        b = tmp
    
    return a
