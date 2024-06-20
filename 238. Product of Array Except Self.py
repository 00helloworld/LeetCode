class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Two Pointers
        res = [1] * len(nums)
        i = 1
        j = len(nums) - 2

        pre = 1
        post = 1

        while i <= len(nums)-1:
            pre = pre * nums[i-1]
            post = post * nums[j+1]
            res[i] = res[i] * pre
            res[j] = res[j] * post
            i += 1
            j -= 1

        return res

