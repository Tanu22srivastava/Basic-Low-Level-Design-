class Board:
    def __init__(self,n):
        self.size= n
        self.board= [[' ' for _ in range(n)] for _ in range(n)]
    
    def display(self):
        for row in self.board:
            print("|".join(row))
            print("-" * (len(row) *2 - 1))
    
    def place_move(self,row,col,symbol):
        if self.board[row][col]==" ":
            self.board[row][col]= symbol
            return True
        return False

    def check_for_win(self,symbol):
        for i in range(self.size):
            if all(self.board[i][j]==symbol for j in range(self.size)) or\
            all(self.board[j][i]==symbol for j in range(self.size)):
                return True

        if all(self.board[i][i]==symbol for i in range(self.size)) or\
        all(self.board[i][self.size-i-1] == symbol for i in range(self.size)):
            return True
        
        return False
    
    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell==" ":
                    return False
        return True
    
