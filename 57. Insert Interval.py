class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        l = newInterval[0]
        r = newInterval[1]
        for itv in intervals:
            if r < itv[0]:
                res.append([l, r])
            if itv[1] < l:
                res.append(itv)
            else:
                l = min(itv[0], l)
                r = max(itv[1], r)

            if 

[1, 5] [7, 8] [10, 12]
