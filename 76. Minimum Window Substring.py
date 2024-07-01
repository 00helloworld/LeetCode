class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_len = len(t)
        t_dic = {}
        for i in t:
            if i in t_dic:
                t_dic[i] += 1
            else:
                t_dic[i] = 1
        s_dic = {}

        min_index = -1
        min_len = 0

        for i in range(len(s) - t_len - 1):
            j = i + t_len
            while j <= len(s):
                
