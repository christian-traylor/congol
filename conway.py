import numpy as np
import time

class Cell():
    def __init__(self,row,col,status):
        self.row = row
        self.col = col
        self.status = status

    def check(self, board):
        count = 0
        possibilities = (
            (self.row-1,self.col-1), (self.row-1,self.col), (self.row-1,self.col+1), (self.row,self.col-1), 
            (self.row,self.col+1), (self.row+1,self.col-1), (self.row+1,self.col), (self.row+1,self.col+1) 
        )

        for cord in possibilities:
            if (cord[0] < 10) and (cord[1] < 10) and (cord[0] > -1) and (cord[1] > -1):
                if board[cord[0]][cord[1]].status == True:
                    count+=1
        
        if (self.status and count == 2) or count == 3:
            return self.row,self.col,True
        else:
            return self.row,self.col,False

    def __repr__(self):
        return "." if self.status else "0"

class Board():
    #TODO: Change seed to work with user input
    def __init__(self,x):
        self.x = x
        self.y = x
        self.board = np.zeros((self.x, self.y), dtype=Cell)
        self.seed = int(np.random.randint(0,high=1000))

    def populate(self):
        np.random.seed(self.seed)
        for x in range(self.x):
            for y in range(self.y): 
                random_int = np.random.randint(0,101)
                self.board[x][y] = Cell(x,y, True if random_int > 40 else False)
                
    def check_cells(self):
        tempBoard = np.zeros((self.x,self.y), dtype=Cell)
        for row in self.board:
            for col in range(len(row)):
                rowPos, colPos, status = row[col].check(self.board)
                tempBoard[rowPos][colPos] = Cell(rowPos,colPos,status)
        self.board = tempBoard

    def __repr__(self):
            return str(self.board)

def main():
    board = Board(10)
    board.populate()
    while True:
        time.sleep(0.8)
        print(board)
        board.check_cells()

if __name__ == "__main__":
    main()