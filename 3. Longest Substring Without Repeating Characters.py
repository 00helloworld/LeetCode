class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        tmp = 0
        i = 0
        for j in range(len(s)):
            if s[j] not in s[i:j]:
                tmp = j - i + 1
                res = max(res, tmp)
            else:
                i = i + s[i:j].index(s[j]) + 1

        return res