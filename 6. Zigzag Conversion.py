class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        res_l = []

        tmp = [''] * (2*numRows-2)
        for i in range(len(s)):
            tmp[i % (2*numRows-2)] = s[i]

        res = ''
        for i in range(numRows):
            for j in range(len(res_l)):
                res += res_l[j][i]

        return res

s = "PAYPALISHIRING"
numRows = 4
so = Solution()
so.convert(s=s, numRows=numRows)
