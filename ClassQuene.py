class Queen:

    def __init__(self, N):
        self.N = N
        self.board = [[0 for i in range(N)]for j in range(N)]
        self.solveQ(0)
    

    def chess_check (self, row, col):
        for i in range(col):
            if self.board[row][i]==1:
                return False
        for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j]==1:
                return False
        for i,j in zip(range(row, self.N, 1), range(col, -1, -1)):
            if self.board[i][j]==1:
                return False
        return True



    def solveQ(self, col):
        if col >= self.N:
            return True

        for i in range(self.N):
            if self.chess_check (i, col):
                self.board[i][col]=1

                if self.solveQ(col+1)==True:
                    return True
                self.board[i][col]=0
            
        return False
    

    def getBoard (self):
        return self.
