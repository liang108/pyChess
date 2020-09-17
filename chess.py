class Piece:
    def __init__(self, init_row, init_col, team):
        self.row = init_row
        self.col = init_col
        self.color = team
        self.position = [self.row, self.col]
        self.moves = [self.row, self.col]


class Pawn(Piece):
    def __init__(self, init_row, init_col, team):
        if team == "white":
            self.symbol = "P"
        if team == "black":
            self.symbol = "p"
        Piece.__init__(self, init_row, init_col, team)

    def __str__(self):
        print(self.symbol)
    
    def CheckMoves(self, board):
        self.moves = [self.row, self.col]   

        # Based on Pawn's color, we want to build a list of possible positions for the pawn to move to

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
    

# board is an 8x8 matrix, or list of lists. Use lists since you want to be able to change values of squares
# board[i][j] To access a square. i represents the row (file), and j represents the column (rank)
# board[0][0] would be the bottom left square from the perspective of the player with white pieces 
# board[7][7] would be the bottom left square from the perspective of the player with black pieces
# board[4][3] would be "d5" in algebraic chess representation
# Empty spaces are represented with 0

class Board: 
    def __init__(self):
        #TODO: rewrite this with object representations instead of strings, then write string representation
        #self.matrix = [["R", "Kn", "B", "Q", "K", "B", "Kn", "R"], ["P", "P", "P", "P", "P", "P", "P", "P"], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], ["p", "p", "p", "p", "p", "p", "p", "p"], ["r", "kn", "b", "q", "k", "b", "kn", "r"]]


    def __str__(self):
        i = 7
        

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
            print("Not a valid move.")
            return False
        else:
            self.matrix[piece.row][piece.col] = 0       
            self.matrix[new_row][new_col] = piece.symbol 
            piece.row = new_row
            piece.col = new_col
            piece.position = [piece.row, piece.col]
            return True
