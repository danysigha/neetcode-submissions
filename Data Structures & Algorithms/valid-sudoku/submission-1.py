class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for row in board:
            for item in row:
                if item.isdigit() and item in seen:
                    return False
                seen.add(item)
            seen.clear()
        
        for index in range(9):
            for row in board:
                if row[index].isdigit() and row[index] in seen:
                    return False
                seen.add(row[index])
            seen.clear()
        
        for i in range(0, 9, 3):
            rows = board[i:i+3]

            for j in range(0, 9, 3):
                for row in rows:
                    for item in row[j:j+3]:
                        if item.isdigit() and item in seen:
                            return False
                        seen.add(item)
                
                seen.clear()

        return True