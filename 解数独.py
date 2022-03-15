class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def backtrack(board, i, j):
            m, n = 9, 9
            if j == n:
                return backtrack(board, i + 1, 0)
            if i == m:
                return True
            if board[i][j] != '.':
                return backtrack(board, i, j + 1)
            for ch in range(1, 10):
                if isValid(board, i, j, ch) is False:
                    continue

                board[i][j] = str(ch)
                if backtrack(board, i, j + 1):
                    return True
                board[i][j] = '.'
            return False

        def isValid(board, row, col, n):
            for i in range(9):
                if board[row][i] == n:
                    return False
                if board[i][col] == n:
                    return False
                if board[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == n:
                    return False
            return True

        backtrack(board, 0, 0)
