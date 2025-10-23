class XO:
    def __init__(self):
        self.currentPlayer = 'X'
        self.createBoard()
        # self.displayBoard()
        self.play()

    def createBoard(self):
        # self.board = [['', '', ''],
        #               ['', '', ''],
        #               ['', '', '']]
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        # print(self.board)

    def displayBoard(self):
        # print(self.board)
        for row in self.board:
            # print(row)
            # for col in row:
            #     print(col, end='\t|')
            print('|'.join(row))
            print('_____')
    def checkWin(self):
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == self.currentPlayer:
                return True
        for x in range (3):
            if self.board[x][0] == self.board[x][1] == self.board[x][2] == self.currentPlayer:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2]== self.currentPlayer:
                return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0]== self.currentPlayer:
                return True
        return False
    def checkDraw(self):
        for i in range(3):
            for x in range(3):
                if self.board[i][x]==" ":
                    return False
        return True
        
    def play(self):
        while True:
            self.displayBoard()

            # Choice 
            row, col = eval(
                input(f"Player{self.currentPlayer}\nEnter row and column: "))
            if self.board[row][col]!= " ":
                print("full")
                continue
            self.board[row][col] = self.currentPlayer
            if self.checkWin():
                print(f"{self.currentPlayer} win")
                break
            if self.checkDraw():
                print("its draw")
                break
            self.currentPlayer = "O" if self.currentPlayer == "X" else "X"
            

XO()
