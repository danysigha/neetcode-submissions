class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowmap = dict()
        colmap = dict()
        squaremap = dict()

        for row in range(9):
            rowmap[row] = set()
            for col in range(9):
                isdigit = board[row][col].isdigit()
                item = board[row][col]
                square_idx = (row // 3, col // 3)
                if squaremap.get(square_idx, False):
                    if isdigit and item in squaremap[square_idx]:
                        return False
                    else:
                        squaremap[square_idx].add(item)
                else:
                    squaremap[square_idx] = set()
                    squaremap[square_idx].add(item)

                if colmap.get(col, False):
                    if isdigit and item in colmap[col]:
                        return False
                    else:
                        colmap[col].add(item)
                else:
                    colmap[col] = set()
                    colmap[col].add(item)
                
                if isdigit and item in rowmap[row]:
                    return False
                    pass
                else:
                    rowmap[row].add(item)
            
        # print(rowmap)
        # print(colmap)
        # print(squaremap)
        return True