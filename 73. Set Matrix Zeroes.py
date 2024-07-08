class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        column_arr = set()
        row_arr = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    column_arr.add(j)
                    row_arr.add(i)
                
        for r in row_arr:
            for j in range(len(matrix[0])):
                matrix[r][j] = 0

        for c in column_arr:
            for i in range(len(matrix)):
                matrix[i][c] = 0

                


                