class Solution(object):
    def isHappy(self, n):
        seen_num = set()
        while n != 1 and n not in seen_num: 
            seen_num.add(n)
            n = sum(int(digit) **2 for digit in str(n))
        return n==1