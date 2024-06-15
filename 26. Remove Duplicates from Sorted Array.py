class Solution(object):
    def removeDuplicates(self, nums):
        # Two Pointers
        
        # the pointer to find the next unique value compared to nums[j]
        i = 1
        # the pointer indicate the last value of current found unique values to compare with nums[i]
        j = 0

        if len(nums) == 0:
            return 0

        while i < len(nums):  # attention edege conditions
            if nums[i] == nums[j]:
                i += 1
            else:
                nums[j+1] = nums[i]
                j += 1

        return j + 1
    
s = Solution()
nums = [1, 2, 2, 4, 5]
print(s.removeDuplicates(nums))
print(nums)

