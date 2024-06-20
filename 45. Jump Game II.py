class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # BFS
        '''
        Hint
        Index:            0 1 2 3 4 5 6 7 8 9 0
        Steps to Reach:   0 1 1 1 2 2 2 3 3 3 3
        '''
        cur_end = 0
        step = 0
        max_end = 0

        for i in range(len(nums)-1):
            max_end = max(i+nums[i], max_end)
            if i == cur_end:
                step += 1
                cur_end = max_end
            
                if max_end >= len(nums)-1:
                    return step
            
        return step
        
    

nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
# nums = [2,3,1,1,4]

s = Solution()
print(s.jump(nums))