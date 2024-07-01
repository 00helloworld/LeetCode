class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        dic_row = [{} for i in range(9)]
        dic_col = [{} for i in range(9)]
        doc_grid = [{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in dic_row[i]:
                    return False
                else:
                    dic_row[i][board[i][j]] = 1

                if board[i][j] in dic_col[j]:
                    return False
                else:
                    dic_col[j][board[i][j]] = 1

                a, b = i // 3, j // 3
                c = a * 3 + b
                if board[i][j] in doc_grid[c]:
                    return False
                else:
                    doc_grid[c][board[i][j]] = 1
        
        return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s = Solution()
s.isValidSudoku(board)