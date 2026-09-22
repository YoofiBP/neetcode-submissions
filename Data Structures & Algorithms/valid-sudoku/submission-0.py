class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                entry = board[row][col]
                if entry == ".":
                    continue
                col_grid = col // 3
                row_grid = row //3
                
                if entry in seen[f"r_{row}"] or entry in seen[f"c_{col}"] or entry in seen[f"{row_grid}_{col_grid}"]:
                    print(False)
                    return False
                else:
                    seen[f"r_{row}"].add(entry)
                    seen[f"c_{col}"].add(entry)
                    seen[f"{row_grid}_{col_grid}"].add(entry)

        print(True)
        return True