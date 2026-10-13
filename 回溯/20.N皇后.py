class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chessboard = ["." * n for _ in range(n)]
        result = []
        self.trace(chessboard, n, 0, result)
        return result

    def trace(self, chessboard, n, row, result):
        if row >= n:
            result.append(chessboard[:])
            return
        for i in range(n):
            if self.isSatisfy(row, i, chessboard, n):
                chessboard[row] = chessboard[row][:i] + "Q" + chessboard[row][i + 1 :]
                self.trace(chessboard, n, row + 1, result)
                chessboard[row] = chessboard[row][:i] + "." + chessboard[row][i + 1 :]

    def isSatisfy(self, row, col, chessboard, n):
        for i in range(n):
            for j in range(n):
                if chessboard[i][j] == "Q":
                    if row == i or j == col:
                        return False
                    if i + j == row + col or i - j == row - col:
                        return False
        return True
