class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
    
        prefix = strs[0]
        
        # Compare the prefix with each string in the array
        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        
        return prefix
        