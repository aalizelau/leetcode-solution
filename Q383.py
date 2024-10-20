class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        char_counts= Counter(magazine)

        for char in ransomNote:
            if char_counts[char]>0:
                char_counts[char] -= 1
            else:
                return False
        return True