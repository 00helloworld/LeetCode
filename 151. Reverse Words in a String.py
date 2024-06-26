class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Trick
        l = s.split()
        l = l[::-1]
        return ' '.join(l)
        
        # Normal
        res = ''
        i = 0
        j = 0
        while i < len(s):
            if s[i] != ' ':
                j = i
                while j < len(s):
                    if s[j] == ' ':
                        word = s[i: j]
                        res = word + ' ' + res
                        i = j
                        break
                    j += 1
                if j == len(s) and s[j-1] != ' ':
                    word = s[i: j]
                    res = word + ' ' + res
                    i = j + 1
            i += 1

        return res.strip()
    
s = "the sky is blue"
so = Solution()
so.reverseWords(s)



        