class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # Brutal time exceeded
        # res = 0
        # for i in range(1, len(nums) + 1):
        #     for j in range(len(nums)-i+1):
        #         if sum(nums[j:j+i]) >= target:
        #             return i
                
        # return res

        # sliding window
        l = 0
        sum = 0
        min_len = len(nums)
        flag = 0
        for r in range(len(nums)):
            sum += nums[r]
            if sum >= target:
                flag = 1
                while l <= r:
                    if sum - nums[l] >= target:
                        sum -= nums[l]
                        min_len = min(r - l, min_len)
                        l += 1
                    else:
                        min_len = min(r - l + 1, min_len)
                        break

                    

        if flag == 0:
            return 0
        else:
            return min_len
        

target = 6
nums = [10,2,3]
s = Solution()
s.minSubArrayLen(target, nums)