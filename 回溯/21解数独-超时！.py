class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        result = [[0] * 9 for _ in range(9)]
        self.trace(board, result, 0, 0)
        for i in range(9):
            for j in range(9):
                board[i][j] = result[i][j]

    def trace(self, board, result, row, col):
        if row >= 9:
            res = [[0] * 9 for _ in range(9)]
            for i in range(9):
                for j in range(9):
                    result[i][j] = board[i][j]
            return

        if board[row][col] == ".":
            for num in range(1, 10):
                if self.isVaild(board, row, col, str(num)):
                    board[row][col] = str(num)
                    if col == 8:
                        self.trace(board, result, row + 1, 0)
                    else:
                        self.trace(board, result, row, col + 1)
                    board[row][col] = "."
        else:
            if col == 8:
                self.trace(board, result, row + 1, 0)
            else:
                self.trace(board, result, row, col + 1)

    def isVaild(self, board, row, col, value):
        for i in range(9):
            if board[row][i] == value or board[i][col] == value:
                return False

        startRow = (int)(row / 3) * 3
        startCol = (int)(col / 3) * 3
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if board[i][j] == value:
                    return False

        return True
