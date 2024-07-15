class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dic = {}
        t_dic = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in s_dic:
                s_dic[s[i]] = 1
            else:
                s_dic[s[i]] += 1

            if t[i] not in t_dic:
                t_dic[t[i]] = 1
            else:
                t_dic[t[i]] += 1

        if s_dic == t_dic:
            return True
        else:
            return False