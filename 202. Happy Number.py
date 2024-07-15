class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = {}
        while True:
            s_n = list(str(n))
            sq_sum = sum([int(i)**2 for i in s_n])
            if sq_sum == 1:
                return True
            elif sq_sum in dic:
                return False
            else:
                dic[n] = sq_sum
                n = sq_sum