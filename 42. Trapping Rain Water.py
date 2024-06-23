class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # append比固定list更慢
        n = len(height)
        if n < 3:
            return 0
        res = 0
        max_l = [0] * n
        max_r = [0] * n
        for i in range(n):
            if i == 0:
                max_l[0] = height[0]
                max_r[0] = height[-1]
            else:
                max_l[i] = max(max_l[i-1], height[i])
                max_r[i] = max(max_r[i-1], height[n-i-1])

        for i in range(n):
            tmp = min(max_l[i], max_r[n-i-1]) - height[i]
            res = res + tmp

        return res
                
            
height = [4,2,0,3,2,5]
s = Solution()
print(s.trap(height))