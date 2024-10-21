import re

class Solution(object):
    def isPalindrome(self, s):
        k=0
        j=-1
        lower_text = s.lower()
        cleaned_text = re.sub(r'[^a-z0-9]', '', lower_text)

        for i in range(len(cleaned_text)//2):
            if cleaned_text[k] == cleaned_text[j]:
                k += 1
                j -= 1
            else:
                return False
        return True 
        
        