class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # two pointers and a cnt
        # same approach with 26
        i = 1
        j = 0
        cnt = 1

        if len(nums) == 0:
            return 0

        while i < len(nums):
            if nums[i] != nums[j]:
                nums[j+1] = nums[i]
                j += 1
                cnt = 1
            else:
                if cnt == 1:
                    nums[j+1] = nums[i]
                    j += 1
                cnt += 1
            i += 1

        return j+1
    
s = Solution()
nums = [0,1,1,1,2,3]
print(nums)
print(s.removeDuplicates(nums))
print(nums)

