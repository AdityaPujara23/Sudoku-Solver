from collections import Counter
import numpy as np

class Validate:
    def check_rep(self,row):
        data = (Counter(row)).most_common()
        most_com = ''
        
        for i in data:
            try:
                int(i[0])
                most_com = i
                break
            except:
                pass
            
        if len(most_com) == 0:
            return True
        if int(most_com[1]) > 1:
            return False
        return True
    
    def __init__(self, board: List[List[str]]) -> bool:
        #check rows
        for row in board:
            if self.check_rep(row) == False:
                return False
            
        #check cols
        ar = np.array(board)
        temp = np.rot90(ar)
        for cols in temp:
            if self.check_rep(cols) == False:
                return False
            
        #check boxes
        row_start = 0
        row_upto = 3
        col_start = 0
        col_upto = 3
        row = []
        while col_upto <= 9:
            while row_upto <= 9:
                for i in range(row_start,row_upto):
                    for j in range(col_start,col_upto):
                        row += list(ar[i][j])
                row_start += 3
                row_upto += 3
                if self.check_rep(row) == False:
                    return False
                row = []
            row_start,row_upto = 0,3
            col_start += 3
            col_upto += 3
        
        return True