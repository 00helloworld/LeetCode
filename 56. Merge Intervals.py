class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])
        res = []
        l = intervals[0][0]
        r = intervals[0][1]
        for itv in intervals:
            if itv[0] > r:
                res.append([l, r])
                l = itv[0]
                r = itv[1]
            elif itv[1] > r:
                r = itv[1]
        res.append([l, r])

        return res
        