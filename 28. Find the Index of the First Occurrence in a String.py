class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        i = 0
        j = 0
        res = -1

        if haystack == needle:
            return 0

        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                if j == 0:
                    res = i
                if j == len(needle) - 1:
                    return res
                i += 1
                j += 1
            else:
                i = i+1 if res==-1 else res+1
                res = -1
                j = 0
                
        return -1


haystack = "mississippi"
needle = "issip"
s = Solution()
s.strStr(haystack, needle)