class Piece:
    def __init__(self, init_row, init_col, team):
        if(team not in ["white", "black"]):
            raise Exception("Attempted to initialize with invalid team")
        self.row = init_row
        self.col = init_col
        self.color = team
        self.moves = [self.row, self.col]


class Pawn(Piece):
    def __init__(self, init_row, init_col, team):
        if team == "white":
            self.symbol = "P"
        if team == "black":
            self.symbol = "p"
        Piece.__init__(self, init_row, init_col, team)

    def __str__(self):
        return self.symbol
    
    def CheckMoves(self, board):
        self.moves = [self.row, self.col]

        # We want to build a list of possible positions for the pawn to move to

        if self.color == "white":
            if (self.row + 1 <= 7):                # If pawn is on furthest row then no moves are possible
                if (board[self.row+1][self.col] == 0):      # Basic forward move is possible if square there is empty and is not on edge of board
                    self.moves = self.moves + [self.row+1, self.col]
                if (self.col + 1 <= 7):            # Check if piece not on right edge 
                    if (board[self.row+1][self.col+1] != 0): # Check if right diagonal square is not empty. Need previous condition so we don't access outside array
                        self.moves = self.moves + [self.row+1, self.col+1]
                if (self.col - 1 >= 0):
                    if (board[self.row+1][self.col-1] != 0):    
                        self.moves = self.moves + [self.x-1, self.y+1]

            return self.moves

        if self.color == "black":
            if (self.row - 1 >= 0):
                if (board[self.row-1][self.col] == 0):
                    self.moves = self.moves + [self.row-1, self.col]
            if (self.col - 1 >= 0):     # Right diagonal move is possible if square nonempty (from perspective of player with black pieces)
                if (board[self.row-1][self.col-1] != 0): 
                    self.moves = self.moves + [self.row-1, self.col-1]
            if (self.col + 1 <= 7):     # Left diagonal move is possible if square nonempty
                if (board[self.row-1][self.col+1] != 0 ):
                    self.moves = self.moves + [self.row-1, self.col+1]
            
            return self.moves


class Rook(Piece):
    def __init__(self, init_row, init_col, team):
        if team == "white":
            self.symbol = "R"
        if team == "black":
            self.symbol = "r"
        Piece.__init__(self, init_row, init_col, team)

    def __str__(self):
        return self.symbol

    def CheckMoves(self, board):
        self.moves = [self.row, self.col]

        # Check vertical moves

        if self.row != 7: 
            for i in range(self.row + 1, 8):    # Starting from rook, check squares above rook to see if empty. If a square is not empty, then rook cannot move past it
                if board.matrix[i][self.col] == 0:
                    self.moves = self.moves + [i, self.col]
                else:
                    if board.matrix[i][self.col].color == self.color:
                        break
                    self.moves = self.moves + [i, self.col]
                    break

        if self.row != 0:      # Now check the squares below the rook, starting from the rook and going down
            i = self.row - 1
            while (i >= 0):
                if board.matrix[i][self.col] == 0:
                    self.moves = self.moves + [i, self.col]
                    i = i-1
                else:
                    if board.matrix[i][self.col].color == self.color:
                        break
                    self.moves = self.moves + [i, self.col]
                    break

        # Check horizontal moves

        if self.col != 7:
            for i in range(self.col, 8):
                if board.matrix[self.row][i] == 0:
                    self.moves = self.moves + [self.row, i]
                else:
                    if board.matrix[self.row][i].color == self.color:
                        break
                    self.moves = self.moves + [self.row, i]
                    break

        if self.col != 0:
            i = self.col - 1
            while (i>=0):
                if board.matrix[self.row][i] == 0:
                    self.moves = self.moves + [self.row, i]
                    i = i-1
                else:
                    if board.matrix[self.row][i].color == self.color:
                        break
                    self.moves = self.moves + [self.row, i]
                    break

        return self.moves


class Bishop(Piece):
    def __init__(self, init_row, init_col, team):
        if team == "white":
            self.symbol = "B"
        if team == "black":
            self.symbol = "b"
        Piece.__init__(self, init_row, init_col, team)

    def __str__(self):
        return self.symbol

    def CheckMoves(self, board):
        if self.row != 7:   # Check upper diagonals
            if self.col != 0:   # Check up left diagonal
                i = self.row + 1
                j = self.col - 1
                while (i <= 7 and j>=0):
                    if (board[i][j] != 0):
                        if (board[i][j].color == self.color):
                            break
                        else:
                            self.moves = self.moves + [i, j]
                            break
                    else:
                        self.moves = self.moves + [i,j]
                        i = i + 1
                        j = j - 1
            if self.col != 7:    # Check up right diagonal
                i = self.row + 1
                j = self.col + 1
                while (i<=7 and j<=7):
                    if (board[i][j] != 0):
                        if (board[i][j].color == self.color):
                            break
                        else:
                            self.moves = self.moves + [i,j]
                            break
                    else:
                        self.moves = self.moves + [i,j]
                        i = i + 1
                        j = j + 1

        if self.row != 0:   # Check lower diagonals
            if self.col != 0:   # Check bottom left diagonal            
                i = self.row - 1
                j = self.col - 1
                while (i >= 0 and j >= 0):
                    if (board[i][j] != 0):
                        if (board[i][j].color == self.color):
                            break
                        else:
                            self.moves = self.moves + [i,j]
                            break
                    else:
                        self.moves = self.moves + [i,j]
                        i = i - 1
                        j = j - 1
            if self.col != 7:   # Check bottom right diagonal
                i = self.row - 1
                j = self.col + 1
                while (i >= 0 and j <= 7):
                    if (board[i][j]!= 0):
                        if(board[i][j].color == self.color):
                            break
                        else:
                            self.moves = self.moves + [i,j]
                            break
                    else:
                        self.moves = self.moves + [i,j]
                        i = i - 1
                        j = j + 1

        return self.moves


class Queen(Piece):
    def __init__(self, init_row, init_col, team):
        if team == "white":
            self.symbol = "Q"
        if team == "black":
            self.symbol = "q"
        Piece.__init__(self, init_row, init_col, team)

    def __str__(self):
        return self.symbol

    def CheckMoves(self, board):
        self.moves = [self.row, self.col]

        # Check vertical moves

        if self.row != 7: 
            for i in range(self.row + 1, 8):    # Starting from rook, check squares above rook to see if empty. If a square is not empty, then rook cannot move past it
                if board.matrix[i][self.col] == 0:
                    self.moves = self.moves + [i, self.col]
                else:
                    if board.matrix[i][self.col].color == self.color:
                        break
                    self.moves = self.moves + [i, self.col]
                    break

        if self.row != 0:      # Now check the squares below the rook, starting from the rook and going down
            i = self.row - 1
            while (i >= 0):
                if board.matrix[i][self.col] == 0:
                    self.moves = self.moves + [i, self.col]
                    i = i-1
                else:
                    if board.matrix[i][self.col].color == self.color:
                        break
                    self.moves = self.moves + [i, self.col]
                    break

        # Check horizontal moves

        if self.col != 7:
            for i in range(self.col, 8):
                if board.matrix[self.row][i] == 0:
                    self.moves = self.moves + [self.row, i]
                else:
                    if board.matrix[self.row][i].color == self.color:
                        break
                    self.moves = self.moves + [self.row, i]
                    break

        if self.col != 0:
            i = self.col - 1
            while (i>=0):
                if board.matrix[self.row][i] == 0:
                    self.moves = self.moves + [self.row, i]
                    i = i-1
                else:
                    if board.matrix[self.row][i].color == self.color:
                        break
                    self.moves = self.moves + [self.row, i]
                    break
        
        if self.row != 7:   # Check upper diagonals
            if self.col != 0:   # Check up left diagonal
                i = self.row + 1
                j = self.col - 1
                while (i <= 7 and j>=0):
                    if (board[i][j] != 0):
                        if (board[i][j].color == self.color):
                            break
                        else:
                            self.moves = self.moves + [i, j]
                            break
                    else:
                        self.moves = self.moves + [i,j]
                        i = i + 1
                        j = j - 1
            if self.col != 7:    # Check up right diagonal
                i = self.row + 1
                j = self.col + 1
                while (i<=7 and j<=7):
                    if (board[i][j] != 0):
                        if (board[i][j].color == self.color):
                            break
                        else:
                            self.moves = self.moves + [i,j]
                            break
                    else:
                        self.moves = self.moves + [i,j]
                        i = i + 1
                        j = j + 1

        if self.row != 0:   # Check lower diagonals
            if self.col != 0:   # Check bottom left diagonal            
                i = self.row - 1
                j = self.col - 1
                while (i >= 0 and j >= 0):
                    if (board[i][j] != 0):
                        if (board[i][j].color == self.color):
                            break
                        else:
                            self.moves = self.moves + [i,j]
                            break
                    else:
                        self.moves = self.moves + [i,j]
                        i = i - 1
                        j = j - 1
            if self.col != 7:   # Check bottom right diagonal
                i = self.row - 1
                j = self.col + 1
                while (i >= 0 and j <= 7):
                    if (board[i][j]!= 0):
                        if(board[i][j].color == self.color):
                            break
                        else:
                            self.moves = self.moves + [i,j]
                            break
                    else:
                        self.moves = self.moves + [i,j]
                        i = i - 1
                        j = j + 1
            
        return self.moves

class King(Piece):
    def __init__(self, init_row, init_col, team):
        if team == "white":
            self.symbol = "K"
        if team == "black":
            self.symbol = "k"
        Piece.__init__(self, init_row, init_col, team)

    def __str__(self):
        return self.symbol

    def CheckMoves(self, board):
        self.moves = [self.row, self.col]

        if self.row != 7:   # Check moves above
            if self.col != 0:
                if (board[self.row+1][self.col-1] == 0):
                    self.moves = self.moves + [self.row+1, self.col-1]
                else:
                    if (board[self.row+1][self.col-1].color != self.color):
                        self.moves = self.moves + [self.row+1, self.col-1]
            if (board[self.row+1][self.col] == 0):
                self.moves = self.moves + [self.row+1, self.col]    
            if (board[self.row+1][self.col] != 0):
                if (board[self.row+1][self.col].color != self.color):
                    self.moves = self.moves + [self.row+1, self.col]
            if self.col != 7:
                if (board[self.row+1][self.col+1] == 0):
                    self.moves = self.moves + [self.row+1, self.col-1]
                else:
                    if (board[self.row+1][self.col+1].color != self.color):
                        self.moves = self.moves + [self.row+1, self.col-1]
        
        if self.row != 0:   # Check moves below
            if self.col != 0:
                if (board[self.row-1][self.col-1] == 0):
                    self.moves = self.moves + [self.row-1, self.col-1]
                else:
                    if(board[self.row-1][self.col-1].color != self.color):
                        self.moves = self.moves + [self.row-1, self.col-1]
            if (board[self.row-1][self.col] != 0):
                if (board[self.row-1][self.col].color != self.color):
                    self.moves = self.moves + [self.row-1, self.col]
            if (board[self.row-1][self.col == 0]):
                self.moves = self.moves + [self.row-1, self.col]

            # TODO: BOTTOM RIGHT SQUARE, LEFT AND RIGHT SQUARES
    

class Board: 
    # board is an 8x8 matrix. Use lists since you want to be able to change values of squares
    # board[i][j] To access a square. i represents the row (file), and j represents the column (rank)
    # board[0][0] would be the bottom left square from the perspective of the player with white pieces 
    # board[7][7] would be the bottom left square from the perspective of the player with black pieces
    # board[4][3] would be "d5" in algebraic chess representation
    # Empty spaces are represented with 0
    def __init__(self):
        #TODO: rewrite this with object representations instead of strings, then write string representation
        self.matrix = [["R", "Kn", "B", "Q", "K", "B", "Kn", "R"], ["P", "P", "P", "P", "P", "P", "P", "P"], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], ["p", "p", "p", "p", "p", "p", "p", "p"], ["r", "kn", "b", "q", "k", "b", "kn", "r"]]


    def Display(self):
        new_matrix = self.matrix[:]
        new_matrix.reverse()

        for row in new_matrix:
            print('\t'.join(map(str,row)))

        print("")
        

    def CheckInProgress(self):    # Game ends when a King has been taken, or checkmate. Todo: Check for checkmate
        white_king = False  # True indicates that piece is still in play
        black_king = False 

        for row in self.matrix:
            if("K" in row): 
                white_king = True
            if("k" in row):
                black_king = True
        
        if (white_king == True) and (black_king == True):
            return True
        else:
            return False

    def MovePiece(self, piece, new_row, new_col):  # Return True if move was made, False if move was not possible
        legal_moves = CheckMoves(piece)
        if [new_row, new_col] not in legal_moves:
            print("Not a valid move, try again.")
            return False
        else:
            self.matrix[piece.row][piece.col] = 0       
            self.matrix[new_row][new_col] = piece.symbol 
            piece.row = new_row
            piece.col = new_col
            piece.position = [piece.row, piece.col]
            return True