class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Back Track
        if len(nums) == 1:
            return True
        
        previous_index = len(nums) - 2
        jump = 1

        while previous_index > 0:
            if nums[previous_index] < jump:
                jump += 1
            else:
                jump = 1
            previous_index -= 1

        if nums[0] < jump:
            return False
        else:
            return True
