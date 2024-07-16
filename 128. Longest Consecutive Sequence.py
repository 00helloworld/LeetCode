class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # O(nlog(n))
        # if len(nums)==0:
        #     return 0
        # sort_num = sorted(list(set(nums)))
        # max_ = 1
        # l = 0
        # r = 1
        # while r <= len(sort_num)-1:
        #     if sort_num[r] - sort_num[r-1] == 1:
        #         max_ = max(max_, r-l+1)
        #     else:
        #         l = r

        #     r += 1

        # return max_

        #O(n)
        if len(nums) == 0:
            return 0
        
        longest = 1
        s = set(nums)
        for num in s:
            if num-1 not in s:
                cnt = 1
                x = num
                while x+1 in s:
                    cnt += 1
                    x = x+1
                
                longest = max(longest, cnt)
        return longest
    
nums = [0,-1]

s = Solution()
s.longestConsecutive(nums)
