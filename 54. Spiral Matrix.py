class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        res = []

        while matrix:

            if matrix:
                res += matrix.pop(0)

            if matrix:
                for row in matrix:
                    if row:
                        res.append(row.pop())

            if matrix:
                res += matrix.pop()[::-1]

            if matrix:
                res += [row.pop(0) for row in matrix if row][::-1]

        return res
    

matrix = [[7],[9],[6]]
s = Solution()
s.spiralOrder(matrix)