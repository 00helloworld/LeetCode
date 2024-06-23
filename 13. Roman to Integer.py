class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        res = 0
        for i in range(len(s)):
            cur = m[s[len(s)-1-i]]
            
            if i > 0:
                if s[len(s)-1-i] == 'I' and s[len(s)-i] in ['V', 'X']:
                    res -= cur
                    continue
                if s[len(s)-1-i] == 'X' and s[len(s)-i] in ['L', 'C']:
                    res -= cur
                    continue
                if s[len(s)-1-i] == 'C' and s[len(s)-i] in ['D', 'M']:
                    res -= cur
                    continue
            res += cur

        return res

        