class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box = [[0] * 9 for _ in range(9)]
        for i in range(len(board)):
            row = [0] * 9
            col = [0] * 9
            for j in range(len(board[i])):
                # 1. track each row
                if (board[i][j]) != '.':
                    value = int(board[i][j]) - 1
                    if row[value] == 1:
                        return False
                    row[value] = 1 

                    # 3. track 3x3 sub group
                    if (box[i//3 + (j//3)*3][value]) == 1:
                        return False
                    box[i//3 + (j//3)*3][value] = 1

                # 2. track each col
                if(board[j][i]) == '.':
                    continue
                else:
                    value = int(board[j][i]) - 1
                    if col[value] == 1:
                        return False
                    col[value] = 1 

        return True