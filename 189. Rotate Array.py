class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # calculate remainder
        k_ = k % len(nums)

        nums[:] = nums[-k_:] + nums[:-k_]
        


nums = [1,2,3,4,5,6,7]
k = 3
s = Solution()
s.rotate(nums, k)
print(nums)