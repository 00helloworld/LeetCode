class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        # 暴力
        # h = max(citations)
        # while h >= 0:
        #     cnt = 0
        #     for i in citations:
        #         if i >= h:
        #             cnt += 1
        #     if cnt >= h:
        #         return h
            
        #     h -= 1

        # Sort + Traverse
        citations.sort()
        i = 1
        if citations[-1] == 0:
            return 0
        else:
            while i <= len(citations):
                if citations[-i] < i:
                    return min(citations[-i+1], i-1)
                i += 1

            return len(citations)
            

citations = [1, 1, 3]
s = Solution()
print(s.hIndex(citations))

