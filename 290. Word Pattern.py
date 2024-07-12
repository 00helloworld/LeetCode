class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s_l = s.split(' ')
        map_p = {}
        map_s = {}

        if len(s_l) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in map_p:
                map_p[pattern[i]] = s_l[i]
            elif map_p[pattern[i]] != s_l[i]:
                return False
            
            if s_l[i] not in map_s:
                map_s[s_l[i]] = pattern[i]
            elif map_s[s_l[i]] != pattern[i]:
                return False
            
        return True