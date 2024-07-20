class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        l = 0
        r = 1
        res = []

        while r <= len(nums):
            if r == len(nums) or nums[r] != nums[r-1] + 1:
                if l == r-1:
                    tmp = f'{nums[l]}'
                else:
                    tmp = f'{nums[l]}->{nums[r-1]}'
                res.append(tmp)
                l = r
            r += 1

        return res
    
s = Solution()
print(s.summaryRanges([0,2,3,4,6,8,9]))