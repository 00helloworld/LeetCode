class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        dic_ = {}
        l = 0
        r = 0
        while r <= len(nums)-1:
            if r - l > k:
                del dic_[nums[l]]
                l += 1

            if nums[r] in dic_:
                return True
            else:
                dic_[nums[r]] = 1
            r += 1
        return False