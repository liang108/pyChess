class Piece:
    def __init__(self, init_row, init_col, team):
        if(team not in ["white", "black"]):
            raise Exception("Attempted to initialize with invalid team")
        self.row = init_row
        self.col = init_col
        self.color = team   
        self.moves = [[self.row, self.col]]

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.symbol


class Pawn(Piece):
    def __init__(self, init_row, init_col, team):
        if team == "white":
            self.symbol = "P"
        if team == "black":
            self.symbol = "p"
        Piece.__init__(self, init_row, init_col, team)
    
    def CheckMoves(self, board):
        self.moves = [[self.row, self.col]]

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

        if self.color == "black":
            if (self.row - 1 >= 0):
                if (board.matrix[self.row-1][self.col] == 0):
                    self.moves = self.moves + [[self.row-1, self.col]]
            if (self.col - 1 >= 0):     # Right diagonal move is possible if square nonempty (from perspective of player with black pieces)
                if (board.matrix[self.row-1][self.col-1] == 0): 
                    self.moves = self.moves + [[self.row-1, self.col-1]]
                if (board.matrix[self.row-1][self.col-1] != 0):
                    if (board.matrix[self.row-1][self.col-1].color != self.color):
                        self.moves = self.moves + [[self.row-1, self.col-1]]
            if (self.col + 1 <= 7):     # Left diagonal move is possible if square nonempty
                if (board.matrix[self.row-1][self.col+1] == 0):
                    self.moves = self.moves + [[self.row-1, self.col+1]]
                if (board.matrix[self.row-1][self.col+1] != 0):
                    if (board.matrix[self.row-1][self.col+1].color != self.color ):
                        self.moves = self.moves + [[self.row-1, self.col+1]]
            
        return self.moves


class Rook(Piece):
    def __init__(self, init_row, init_col, team):
        if team == "white":
            self.symbol = "R"
        if team == "black":
            self.symbol = "r"
        Piece.__init__(self, init_row, init_col, team)


    def CheckMoves(self, board):
        self.moves = [[self.row, self.col]]

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
            for i in range(self.col, 8):
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


class Knight(Piece):
    def __init__(self, init_row, init_col, team):
        if team == "white":
            self.symbol = "Kn"
        if team == "black":
            self.symbol = "kn"
        Piece.__init__(self, init_row, init_col, team)

    def CheckMoves(self, board):
        self.moves = [[self.row, self.col]]

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
                if (board.matrix[self.row+2][self.col+1] == 0):
                    self.moves = self.moves + [[self.row-2, self.col+1]]
                else:
                    if (board.matrix[self.row+2][self.col+1].color != self.color):
                        self.moves = self.moves + [[self.row-2, self.col+1]]

        return self.moves


class Bishop(Piece):
    def __init__(self, init_row, init_col, team):
        if team == "white":
            self.symbol = "B"
        if team == "black":
            self.symbol = "b"
        Piece.__init__(self, init_row, init_col, team)


    def CheckMoves(self, board):
        self.moves = [[self.row, self.col]]

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


    def CheckMoves(self, board):
        self.moves = [[self.row, self.col]]

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
        

    def CheckMoves(self, board):
        self.moves = [[self.row, self.col]]


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
                    if (board[self.row-1][self.col-1].color != self.color):
                        self.moves = self.moves + [self.row-1, self.col-1]
            if (board[self.row-1][self.col] != 0):
                if (board[self.row-1][self.col].color != self.color):
                    self.moves = self.moves + [self.row-1, self.col]
            if (board[self.row-1][self.col == 0]):
                self.moves = self.moves + [self.row-1, self.col]
            if self.col != 7:
                if (board[self.row-1][self.col+1] == 0):
                    self.moves = self.moves + [self.row-1, self.col+1]
                else:
                    if (board[self.row-1][self.col+1].color != self.color):
                        self.moves = self.moves + [self.row-1, self.col+1]

        if self.col != 0:   # Check left square
            if (board[self.row][self.col-1] == 0):
                self.moves = self.moves + [self.row, self.col-1]
            else: 
                if (board[self.row][self.col-1].color != self.color):
                    self.moves = self.moves + [self.row, self.col-1]
        
        if self.col != 7:   # Check right square
            if (board[self.row][self.col+1] == 0):
                self.moves = self.moves + [self.row, self.col+1]
            else:
                if (board[self.row][self.col+1].color != self.color):
                    self.moves = self.moves + [self.row, self.col+1]
        
        return self.moves


class Board: 
    def __init__(self):
        # Create pieces

        self.pieces = [Rook(0,0,"white"), Knight(0,1,"white"), Bishop(0,2,"white"), Queen(0,3,"white"), King(0,4,"white"), Bishop(0,5,"white"), Knight(0,6,"white"), Rook(0,7,"white")]

        for i in range(0,8):
            self.pieces.append(Pawn(1,i,"white"))

        for i in range(0,8):
            self.pieces.append(Pawn(6,i,"black"))

        self.pieces = self.pieces + [Rook(7,0,"black"), Knight(7,1,"black"), Bishop(7,2,"black"), Queen(7,3,"black"), King(7,4,"black"), Bishop(7,5,"black"), Knight(7,6,"black"), Rook(7,7,"black")]

        # Initialize board, and place pieces on board

        self.matrix = []
        for i in range(0,8):
            self.matrix.append([0,0,0,0,0,0,0,0])

        for piece in self.pieces:
            self.matrix[piece.row][piece.col] = piece

        #self.matrix = [["R", "Kn", "B", "Q", "K", "B", "Kn", "R"], ["P", "P", "P", "P", "P", "P", "P", "P"], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], ["p", "p", "p", "p", "p", "p", "p", "p"], ["r", "kn", "b", "q", "k", "b", "kn", "r"]]

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
            for piece in row:
                if isinstance(piece, King) == True:
                    if (piece.color == "white"):
                        white_king = True
                    if (piece.color == "black"):
                        black_king = True
        
        if (white_king == True) and (black_king == True):
            return True
        else:
            return False

    def MovePiece(self, init_row, init_col, new_row, new_col):  # Return True if move was made, False if move was not possible
        piece = self.matrix[init_row][init_col]
        legal_moves = piece.CheckMoves(self)

        if [new_row, new_col] not in legal_moves:
            print("Not a valid move, try again.")
            return False

        else:   
            self.matrix[new_row][new_col] = piece
            self.matrix[piece.row][piece.col] = 0 
            piece.row = new_row
            piece.col = new_col
            piece.moves = [piece.row, piece.col]
            return True