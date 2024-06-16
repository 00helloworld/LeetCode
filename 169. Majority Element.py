class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 1. Map
        # M = {}
        # for i in nums:
        #     if i in M:
        #         M[i] += 1
                
        #     else:
        #         M[i] = 1

        #     if M[i] > len(nums)/2:
        #             return i
            
        
        # 2. Sort
        # nums.sort()
        # return nums[len(nums)//2]
    

        # 3. Boyer-Moore Majority Vote Algorithm
        majority = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] == majority:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    majority = nums[i]
                    cnt = 1
        return majority
        





s = Solution()
nums = [2,2,1,1,1,2,2]
print(s.majorityElement(nums))
