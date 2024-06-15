def removeElement(nums, val):
    # Two Pointer

    # the pointer to find value not equal to val
    i = 0  
    # the pointer to find value equal to val, which is goning to be replaced 
    # by next value not equal to val
    j = 0  

    while i < len(nums):
        if nums[i] == val:
            i += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1

    return j

nums = [2, 3, 3, 2]
print(removeElement(nums, 2))
print(nums)
