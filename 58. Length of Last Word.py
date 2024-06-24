class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 正经
        # l = 0
        # for i in range(1, len(s)+1):
        #     if s[-i] != ' ':
        #         l += 1
        #     elif l > 0:
        #         return l
            
        # return l
    
        # trick
        
        return len(s.strip().split(' ')[-1])