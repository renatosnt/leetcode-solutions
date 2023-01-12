class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        bot, top = 0, ROWS - 1

        while bot <= top:
            row = bot + (top - bot) // 2

            if matrix[row][0] > target:
                #primeira metade
                top = row - 1
            elif matrix[row][-1] < target:
                # segunda metade
                bot = row + 1
            else:
                break
        if not (bot <= top):
            return False
        row = bot + (top - bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            mid = l + (r - l) // 2

            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False