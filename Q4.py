class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def backtrack(r, c, first):
            if first == len(word):
                return True
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != word[first]:
                return False

            ret = False
            board[r][c] = "#"
            for rowOffset, colOffset in[(0,1),(1,0),(-1,0),(0,-1)]:
                ret = backtrack(r + rowOffset, c + colOffset, first + 1)
                if ret: break

            board[r][c] = word[first]

            return ret


        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True


