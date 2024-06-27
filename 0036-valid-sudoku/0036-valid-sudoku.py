from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       # Check rows
        for row in board:
            if not self.is_valid_unit(row):
                return False
        
        # Check columns
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.is_valid_unit(column):
                return False
        
        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.is_valid_unit(box):
                    return False
        
        return True
    
    def is_valid_unit(self, unit: List[str]) -> bool:
        unit = [num for num in unit if num != '.']
        return len(unit) == len(set(unit))
