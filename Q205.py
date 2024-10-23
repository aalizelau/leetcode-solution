class Solution(object):
    def isIsomorphic(self, s, t):
        char_map_s_to_t = {}
        char_map_t_to_s = {}

        for i in range(len(s)):
            if s[i] not in char_map_s_to_t:
                if t[i] in char_map_t_to_s and char_map_t_to_s[t[i]] != s[i]:
                    return False 
                char_map_s_to_t[s[i]] = t[i]
                char_map_t_to_s[t[i]] = s[i]
            elif char_map_s_to_t[s[i]] != t[i]:
                return False
        return True