class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic_ = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in dic_:
                dic_[ss].append(s)
            else:
                dic_[ss] = [s]

        return list(dic_.values())