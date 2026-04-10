class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        grid = defaultdict(set)
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if (value == "."):
                    continue
                else:
                    if (value in row[r]) or (value in column[c]) or (value in grid[(r //3, c // 3)]):
                        return False
                    else:
                        row[r].add(value)
                        column[c].add(value)
                        grid[(r //3, c // 3)].add(value)
                
        return True