class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # Sort + Two Pointers
        res = set()
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

        return list(res)