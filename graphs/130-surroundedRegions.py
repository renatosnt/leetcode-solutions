class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or board[r][c] != "O"
            ):
                return
            board[r][c] = "N"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            

        # encontra "O" nas extremidades e roda dfs neles substituindos por N
        for i in range(ROWS):
            for j in range(COLS):
                if (i in [0, ROWS - 1] or j in [0, COLS - 1]) and board[i][j] == "O":
                    dfs(i, j)

        # substitui todos os "O" por "X"
        for i in range(ROWS):
            for j in range(COLS):
                if (board[i][j] == "O"):
                    board[i][j] = "X"
        # substitui todos os N por "O"
        for i in range(ROWS):
            for j in range(COLS):
                if (board[i][j] == "N"):
                    board[i][j] = "O"
  