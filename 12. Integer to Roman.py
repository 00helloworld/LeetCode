class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        '''
        Input: num = 3749
        Output: "MMMDCCXLIX"
        '''

        m = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        res = ''
        if num >= 1000:
            d = num // 1000
            res += d*m[1000]
            num -= d*1000
        if num >= 100:
            d = num // 100
            if d == 4:
                res += m[400]
            elif d == 5:
                res += m[500]
            elif d == 9:
                res += m[900]
            elif d < 4:
                res += d * m[100]
            elif d > 5:
                d_ = d % 5
                res += m[500]+m[100]*d_
            num -= d*100
        if num >= 10:
            d = num // 10
            if d == 4:
                res += m[40]
            elif d == 5:
                res += m[50]
            elif d == 9:
                res += m[90]
            elif d < 4:
                res += d * m[10]
            elif d > 5:
                d_ = d % 5
                res += m[50]+m[10]*d_
            num -= d*10

        if num == 4:
            res += m[4]
        elif num == 5:
            res += m[5]
        elif num == 9:
            res += m[9]
        elif num < 4:
            res += num * m[1]
        elif num > 5:
            d_ = num % 5
            res += m[5]+m[1]*d_

        return res

        


