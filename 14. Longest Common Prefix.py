class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        f = -1
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i > len(strs[j])-1:
                    return res[:-1]
                if j == 0:
                    res += strs[j][i]
                    f += 1
                else:
                    if strs[j][i] != res[f]:
                        return res[:-1]
                    else:
                        continue

        return res