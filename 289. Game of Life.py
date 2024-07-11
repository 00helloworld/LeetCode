class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        tmp = []
        for i in range(len(board)):
            tmp_row = []
            for j in range(len(board[0])):
                row_start = i - 1 if i-1 > 0 else 0
                row_end = i + 2
                col_start = j - 1 if j-1 > 0 else 0
                col_end = j + 2
                area = [row[col_start: col_end] for row in board[row_start: row_end]]
                sum_ = sum(sum(row) for row in area) - board[i][j]
                tmp_row.append(sum_)
            tmp.append(tmp_row)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    if tmp[i][j] == 3:
                        board[i][j] = 1
                else:
                    if tmp[i][j] < 2 or tmp[i][j] > 3:
                        board[i][j] = 0

        return board