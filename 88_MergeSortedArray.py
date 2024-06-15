# double pointer
def merger(nums1, m, nums2, n):
    k = n + m - 1
    i = m - 1
    j = n - 1

    while j >= 0:
        if i < 0 or nums2[j] >= nums1[i]:
            nums1[k] = nums2[j]
            j -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1
        k -= 1

n1 = [1,2,3,0,0,0]

