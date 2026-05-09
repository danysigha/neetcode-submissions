class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowmap = defaultdict(set)
        colmap = defaultdict(set)
        squaremap = defaultdict(set)

        for row in range(9):
            for col in range(9):
                item = board[row][col]

                if item == ".":
                    continue

                if (item in rowmap[row]
                    or item in colmap[col]
                    or item in squaremap[(row // 3, col // 3)]):
                    return False
                
                rowmap[row].add(item)
                colmap[col].add(item)
                squaremap[(row // 3, col // 3)].add(item)
            
        # print(rowmap)
        # print(colmap)
        # print(squaremap)
        return True