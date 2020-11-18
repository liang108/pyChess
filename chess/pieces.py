import pygame


### BASE CLASS ###

class Piece:
    def __init__(self, init_row, init_col, team):
        if(team not in ["white", "black"]):
            raise Exception("Attempted to initialize with invalid team")
        self.row = init_row
        self.col = init_col
        self.color = team   
        self.moves = []
        # Dimensions of chessboard squares
        self.image_height = 37+((635/8)*(7-self.row))
        self.image_width = 37+((634/8)*(self.col))

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.symbol


### PAWN ###


class Pawn(Piece):
    def __init__(self, init_row, init_col, team):
        if team == "white":
            self.symbol = "P"
            self.image = pygame.image.load(r'C:\Users\jhlia\Desktop\chess\Resized\white_pawn.png')
        if team == "black":
            self.symbol = "p"
            self.image = pygame.image.load(r'C:\Users\jhlia\Desktop\chess\Resized\black_pawn.png')
        Piece.__init__(self, init_row, init_col, team)
        self.image_width = 35+((634/8)*(self.col))
    
    def CheckMoves(self, board):
        self.moves = []

        # We want to build a list of possible positions for the pawn to move to

        if self.color == "white":
            if (self.row + 1 <= 7):                # If pawn is on furthest row then no moves are possible
                if (board.matrix[self.row+1][self.col] == 0):      # Basic forward move is possible if square there is empty and is not on edge of board
                    self.moves = self.moves + [[self.row+1, self.col]]
                if (self.col + 1 <= 7):            # Check if piece not on right edge 
                    if (board.matrix[self.row+1][self.col+1] != 0): # Check if right diagonal square is not empty. Need previous condition 
                        if (board.matrix[self.row+1][self.col+1].color != self.color):
                            self.moves = self.moves + [[self.row+1, self.col+1]]
                if (self.col - 1 >= 0):
                    if (board.matrix[self.row+1][self.col-1] == 0):
                        self.moves = self.moves + [[self.row+1, self.col-1]]
                    if (board.matrix[self.row+1][self.col-1] != 0):
                        if (board.matrix[self.row+1][self.col-1].color != self.color):
                            self.moves = self.moves + [[self.row+1, self.col-1]]
            if (self.row == 1):     # Starting position: Can move forward two squares if both empty
                if (board.matrix[self.row+1][self.col] == 0 and board.matrix[self.row+2][self.col] == 0):
                    self.moves = self.moves + [[self.row+2, self.col]]

        if self.color == "black":
            if (self.row - 1 >= 0):
                if (board.matrix[self.row-1][self.col] == 0):
                    self.moves = self.moves + [[self.row-1, self.col]]
            if (self.col - 1 >= 0):     # Right diagonal move is possible if square nonempty (from perspective of player with black pieces)
                if (board.matrix[self.row-1][self.col] == 0): 
                    self.moves = self.moves + [[self.row-1, self.col]]
                if (board.matrix[self.row-1][self.col-1] != 0):
                    if (board.matrix[self.row-1][self.col-1].color != self.color):
                        self.moves = self.moves + [[self.row-1, self.col-1]]
            if (self.col + 1 <= 7):     # Left diagonal move is possible if square nonempty
                if (board.matrix[self.row-1][self.col] == 0):
                    self.moves = self.moves + [[self.row-1, self.col]]
                if (board.matrix[self.row-1][self.col+1] != 0):
                    if (board.matrix[self.row-1][self.col+1].color != self.color ):
                        self.moves = self.moves + [[self.row-1, self.col+1]]
            if (self.row == 6): 
                if (board.matrix[self.row-1][self.col] == 0 and board.matrix[self.row-2][self.col] == 0):
                    self.moves = self.moves + [[self.row-2, self.col]]

            
        return self.moves


### ROOK ###


class Rook(Piece):
    def __init__(self, init_row, init_col, team):
        if team == "white":
            self.symbol = "R"
            self.image = pygame.image.load(r'C:\Users\jhlia\Desktop\chess\Resized\white_rook.png')
        if team == "black":
            self.symbol = "r"
            self.image = pygame.image.load(r'C:\Users\jhlia\Desktop\chess\Resized\black_rook.png')
        Piece.__init__(self, init_row, init_col, team)


    def CheckMoves(self, board):
        self.moves = []

        # Check vertical moves

        if self.row != 7: 
            for i in range(self.row + 1, 8):    # Starting from rook, check squares above rook to see if empty. If a square is not empty, then rook cannot move past it
                if board.matrix[i][self.col] == 0:
                    self.moves = self.moves + [[i, self.col]]
                else:
                    if board.matrix[i][self.col].color == self.color:
                        break
                    self.moves = self.moves + [[i, self.col]]
                    break

        if self.row != 0:      # Now check the squares below the rook, starting from the rook and going down
            i = self.row - 1
            while (i >= 0):
                if board.matrix[i][self.col] == 0:
                    self.moves = self.moves + [[i, self.col]]
                    i = i-1
                else:
                    if board.matrix[i][self.col].color == self.color:
                        break
                    self.moves = self.moves + [[i, self.col]]
                    break

        # Check horizontal moves

        if self.col != 7:
            for i in range(self.col+1, 8):
                if board.matrix[self.row][i] == 0:
                    self.moves = self.moves + [[self.row, i]]
                else:
                    if board.matrix[self.row][i].color == self.color:
                        break
                    self.moves = self.moves + [[self.row, i]]
                    break

        if self.col != 0:
            i = self.col - 1
            while (i>=0):
                if board.matrix[self.row][i] == 0:
                    self.moves = self.moves + [[self.row, i]]
                    i = i-1
                else:
                    if board.matrix[self.row][i].color == self.color:
                        break
                    self.moves = self.moves + [[self.row, i]]
                    break

        return self.moves


### KNIGHT ###


class Knight(Piece):
    def __init__(self, init_row, init_col, team):
        if team == "white":
            self.symbol = "Kn"
            self.image = pygame.image.load(r'C:\Users\jhlia\Desktop\chess\Resized\white_knight.png')
        if team == "black":
            self.symbol = "kn"
            self.image = pygame.image.load(r'C:\Users\jhlia\Desktop\chess\Resized\black_knight.png')
        Piece.__init__(self, init_row, init_col, team)

    def CheckMoves(self, board):
        self.moves = []

        if (self.row + 2 <= 7):
            if (self.col - 1 >= 0):
                if (board.matrix[self.row+2][self.col-1] == 0):
                    self.moves = self.moves + [[self.row+2, self.col-1]]
                else:
                    if (board.matrix[self.row+2][self.col-1].color != self.color):
                        self.moves = self.moves + [[self.row+2, self.col-1]]

            if (self.col + 1 <= 7):
                if (board.matrix[self.row+2][self.col+1] == 0):
                    self.moves = self.moves + [[self.row+2, self.col+1]]
                else:
                    if (board.matrix[self.row+2][self.col+1].color != self.color):
                        self.moves = self.moves + [[self.row+2, self.col+1]]

        if (self.row + 1 <= 7):
            if (self.col - 2 >= 0):
                if (board.matrix[self.row+1][self.col-2] == 0):
                    self.moves = self.moves + [[self.row+1, self.col-2]]
                else:
                    if (board.matrix[self.row+1][self.col-2].color != self.color):
                        self.moves = self.moves + [[self.row+1, self.col-2]]

            if (self.col + 2 <= 7):
                if (board.matrix[self.row+1][self.col+2] == 0):
                    self.moves = self.moves + [[self.row+1, self.col+2]]
                else:
                    if (board.matrix[self.row+1][self.col+2].color != self.color):
                        self.moves = self.moves + [[self.row+1, self.col+2]]

        if (self.row - 1 >= 0):
            if (self.col - 2 >=0):
                if (board.matrix[self.row-1][self.col-2] == 0):
                    self.moves = self.moves + [[self.row-1, self.col-2]]
                else:
                    if (board.matrix[self.row-1][self.col-2].color != self.color):
                        self.moves = self.moves + [[self.row-1, self.col-2]]

            if (self.col + 2 <= 7):
                if (board.matrix[self.row-1][self.col+2] == 0):
                    self.moves = self.moves + [[self.row-1, self.col+2]]
                else:    
                    if (board.matrix[self.row-1][self.col+2].color != self.color):
                        self.moves = self.moves + [[self.row-1, self.col+2]]
        
        if (self.row - 2 >= 0):
            if (self.col - 1 >= 0):
                if (board.matrix[self.row-2][self.col-1] == 0):
                    self.moves = self.moves + [[self.row-2, self.col-1]]
                else:
                    if (board.matrix[self.row-2][self.col-1].color != self.color):
                        self.moves = self.moves + [[self.row-2, self.col-1]]
            if (self.col + 1 <= 7):
                if (board.matrix[self.row-2][self.col+1] == 0):
                    self.moves = self.moves + [[self.row-2, self.col+1]]
                else:
                    if (board.matrix[self.row-2][self.col+1].color != self.color):
                        self.moves = self.moves + [[self.row-2, self.col+1]]

        return self.moves


### BISHOP ###


class Bishop(Piece):
    def __init__(self, init_row, init_col, team):
        if team == "white":
            self.symbol = "B"
            self.image = pygame.image.load(r'C:\Users\jhlia\Desktop\chess\Resized\white_bishop.png')
        if team == "black":
            self.symbol = "b"
            self.image = pygame.image.load(r'C:\Users\jhlia\Desktop\chess\Resized\black_bishop.png')
        Piece.__init__(self, init_row, init_col, team)


    def CheckMoves(self, board):
        self.moves = []

        if self.row != 7:               # Check upper diagonals
            if self.col != 0:           # Check up left diagonal
                i = self.row + 1
                j = self.col - 1
                while (i<=7 and j>=0):
                    if (board.matrix[i][j] != 0):
                        if (board.matrix[i][j].color == self.color):
                            break
                        else:
                            self.moves = self.moves + [[i, j]]
                            break
                    else:
                        self.moves = self.moves + [[i,j]]
                        i = i + 1
                        j = j - 1
            if self.col != 7:           # Check up right diagonal
                i = self.row + 1
                j = self.col + 1
                while (i<=7 and j<=7):
                    if (board.matrix[i][j] != 0):
                        if (board.matrix[i][j].color == self.color):
                            break
                        else:
                            self.moves = self.moves + [[i,j]]
                            break
                    else:
                        self.moves = self.moves + [[i,j]]
                        i = i + 1
                        j = j + 1

        if self.row != 0:               # Check lower diagonals
            if self.col != 0:           # Check bottom left diagonal            
                i = self.row - 1
                j = self.col - 1
                while (i >= 0 and j >= 0):
                    if (board.matrix[i][j] != 0):
                        if (board.matrix[i][j].color == self.color):
                            break
                        else:
                            self.moves = self.moves + [[i,j]]
                            break
                    else:
                        self.moves = self.moves + [[i,j]]
                        i = i - 1
                        j = j - 1
            if self.col != 7:   # Check bottom right diagonal
                i = self.row - 1
                j = self.col + 1
                while (i >= 0 and j <= 7):
                    if (board.matrix[i][j]!= 0):
                        if(board.matrix[i][j].color == self.color):
                            break
                        else:
                            self.moves = self.moves + [[i,j]]
                            break
                    else:
                        self.moves = self.moves + [[i,j]]
                        i = i - 1
                        j = j + 1

        return self.moves


### QUEEN ###


class Queen(Piece):
    def __init__(self, init_row, init_col, team):
        if team == "white":
            self.symbol = "Q"
            self.image = pygame.image.load(r'C:\Users\jhlia\Desktop\chess\Resized\white_queen.png')
        if team == "black":
            self.symbol = "q"
            self.image = pygame.image.load(r'C:\Users\jhlia\Desktop\chess\Resized\black_queen.png')
        Piece.__init__(self, init_row, init_col, team)


    def CheckMoves(self, board):
        self.moves = []

        # Check vertical moves

        if self.row != 7: 
            for i in range(self.row + 1, 8):    # Starting from rook, check squares above rook to see if empty. If a square is not empty, then rook cannot move past it
                if board.matrix[i][self.col] == 0:
                    self.moves = self.moves + [[i, self.col]]
                else:
                    if board.matrix[i][self.col].color == self.color:
                        break
                    self.moves = self.moves + [[i, self.col]]
                    break

        if self.row != 0:      # Now check the squares below the rook, starting from the rook and going down
            i = self.row - 1
            while (i >= 0):
                if board.matrix[i][self.col] == 0:
                    self.moves = self.moves + [[i, self.col]]
                    i = i-1
                else:
                    if board.matrix[i][self.col].color == self.color:
                        break
                    self.moves = self.moves + [[i, self.col]]
                    break

        # Check horizontal moves

        if self.col != 7:
            for i in range(self.col+1, 8):
                if board.matrix[self.row][i] == 0:
                    self.moves = self.moves + [[self.row, i]]
                else:
                    if board.matrix[self.row][i].color == self.color:
                        break
                    self.moves = self.moves + [[self.row, i]]
                    break

        if self.col != 0:
            i = self.col - 1
            while (i>=0):
                if board.matrix[self.row][i] == 0:
                    self.moves = self.moves + [[self.row, i]]
                    i = i-1
                else:
                    if board.matrix[self.row][i].color == self.color:
                        break
                    self.moves = self.moves + [[self.row, i]]
                    break
        
        if self.row != 7:   # Check upper diagonals
            if self.col != 0:   # Check up left diagonal
                i = self.row + 1
                j = self.col - 1
                while (i<=7 and j>=0):
                    if (board.matrix[i][j] != 0):
                        if (board.matrix[i][j].color == self.color):
                            break
                        else:
                            self.moves = self.moves + [[i, j]]
                            break
                    else:
                        self.moves = self.moves + [[i,j]]
                        i = i + 1
                        j = j - 1
            if self.col != 7:    # Check up right diagonal
                i = self.row + 1
                j = self.col + 1
                while (i<=7 and j<=7):
                    if (board.matrix[i][j] != 0):
                        if (board.matrix[i][j].color == self.color):
                            break
                        else:
                            self.moves = self.moves + [[i,j]]
                            break
                    else:
                        self.moves = self.moves + [[i,j]]
                        i = i + 1
                        j = j + 1

        if self.row != 0:   # Check lower diagonals
            if self.col != 0:   # Check bottom left diagonal            
                i = self.row - 1
                j = self.col - 1
                while (i >= 0 and j >= 0):
                    if (board.matrix[i][j] != 0):
                        if (board.matrix[i][j].color == self.color):
                            break
                        else:
                            self.moves = self.moves + [[i,j]]
                            break
                    else:
                        self.moves = self.moves + [[i,j]]
                        i = i - 1
                        j = j - 1
            if self.col != 7:   # Check bottom right diagonal
                i = self.row - 1
                j = self.col + 1
                while (i >= 0 and j <= 7):
                    if (board.matrix[i][j]!= 0):
                        if(board.matrix[i][j].color == self.color):
                            break
                        else:
                            self.moves = self.moves + [[i,j]]
                            break
                    else:
                        self.moves = self.moves + [[i,j]]
                        i = i - 1
                        j = j + 1
            
        return self.moves


### KING ###


class King(Piece):
    def __init__(self, init_row, init_col, team):
        if team == "white":
            self.symbol = "K"
            self.image = pygame.image.load(r'C:\Users\jhlia\Desktop\chess\Resized\white_king.png')
        if team == "black":
            self.symbol = "k"
            self.image = pygame.image.load(r'C:\Users\jhlia\Desktop\chess\Resized\black_king.png')
        Piece.__init__(self, init_row, init_col, team)
        

    def CheckMoves(self, board):
        self.moves = []

        if self.row != 7:   # Check moves above
            if self.col != 0:
                if (board.matrix[self.row+1][self.col-1] == 0):
                    self.moves = self.moves + [[self.row+1, self.col-1]]
                else:
                    if (board.matrix[self.row+1][self.col-1].color != self.color):
                        self.moves = self.moves + [[self.row+1, self.col-1]]
            if (board.matrix[self.row+1][self.col] == 0):
                self.moves = self.moves + [[self.row+1, self.col]] 
            if (board.matrix[self.row+1][self.col] != 0):
                if (board.matrix[self.row+1][self.col].color != self.color):
                    self.moves = self.moves + [[self.row+1, self.col]]
            if self.col != 7:
                if (board.matrix[self.row+1][self.col+1] == 0):
                    self.moves = self.moves + [[self.row+1, self.col+1]]
                else:
                    if (board.matrix[self.row+1][self.col+1].color != self.color):
                        self.moves = self.moves + [[self.row+1, self.col+1]]
        
        if self.row != 0:   # Check moves below
            if self.col != 0:
                if (board.matrix[self.row-1][self.col-1] == 0):
                    self.moves = self.moves + [[self.row-1, self.col-1]]
                else:
                    if (board.matrix[self.row-1][self.col-1].color != self.color):
                        self.moves = self.moves + [[self.row-1, self.col-1]]
            if (board.matrix[self.row-1][self.col] != 0):
                if (board.matrix[self.row-1][self.col].color != self.color):
                    self.moves = self.moves + [[self.row-1, self.col]]
            if (board.matrix[self.row-1][self.col == 0]):
                self.moves = self.moves + [[self.row-1, self.col]]
            if self.col != 7:
                if (board.matrix[self.row-1][self.col+1] == 0):
                    self.moves = self.moves + [[self.row-1, self.col+1]]
                else:
                    if (board.matrix[self.row-1][self.col+1].color != self.color):
                        self.moves = self.moves + [[self.row-1, self.col+1]]

        if self.col != 0:   # Check left square
            if (board.matrix[self.row][self.col-1] == 0):
                self.moves = self.moves + [[self.row, self.col-1]]
            else: 
                if (board.matrix[self.row][self.col-1].color != self.color):
                    self.moves = self.moves + [[self.row, self.col-1]]
        
        if self.col != 7:   # Check right square
            if (board.matrix[self.row][self.col+1] == 0):
                self.moves = self.moves + [[self.row, self.col+1]]
            else:
                if (board.matrix[self.row][self.col+1].color != self.color):
                    self.moves = self.moves + [[self.row, self.col+1]]
        
        return self.moves
