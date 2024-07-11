class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        map_m = {}
        for i in magazine:
            if i not in map_m:
                map_m[i] = 1
            else:
                map_m[i] += 1

        for i in ransomNote:
            if i not in map_m or map_m[i] < 1:
                return False
            else:
                map_m[i] -= 1
        
        return True