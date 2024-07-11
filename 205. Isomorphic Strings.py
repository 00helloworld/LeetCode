class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m_s = {}
        m_t = {}

        for i in range(len(s)):
            if s[i] not in m_s:
                m_s[s[i]] = t[i]
            elif m_s[s[i]] != t[i]:
                return False
            
            if t[i] not in m_t:
                m_t[t[i]] = s[i]
            elif m_t[t[i]] != s[i]:
                return False
            
        return True