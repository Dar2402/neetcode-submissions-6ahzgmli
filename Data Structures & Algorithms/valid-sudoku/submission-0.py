class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            s = set()
            for c in r:
                if c in s:
                    return False
                elif c != ".":
                    s.add(c)
                    
        
        for r in range(9):
            s = set()
            for c in range(9):
                e = board[c][r]
                if e in s:
                    return False
                elif e != ".":
                    s.add(e)
        
        s = {}
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                key = (r // 3, c // 3)
                
                if key not in s:
                    s[key] = set()
                
                
                if val in s[key]:
                    return False
                elif val != ".":
                    s[key].add(val)
        
        return True
        