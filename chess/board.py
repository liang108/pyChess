import pygame
import pieces

# Includes game loop

class Board: 

    def __init__(self):
        self.colDict = {"a":0, "A":0, "b":1, "B":1, "c":2, "C":2, "d":3, "D":3, "e":4, "E":4, "f":5, "F":5, "g":6, "G":6, "h":7, "H":7} # This helps player translate input position from algebraic notation to array notation

        # Initialize board, and place pieces on board
        self.ResetBoard()

    def Display_Text(self):
        new_matrix = self.matrix[:]
        new_matrix.reverse()
        i=8
        for row in new_matrix:
            print(str(i)+ '\t\t' + '\t'.join(map(str,row)))
            print("")
            i = i-1

        print("")
        print("")
        print('\t\tA\tB\tC\tD\tE\tF\tG\tH')
        print("")
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
        
        if (white_king == True) and (black_king == False):
            print("Player 1 Wins!")
            return False
        elif (white_king == False) and (black_king == True):
            print("Player 2 Wins!")
            return False
        else:
            return True

    def MovePiece(self, init_col, init_row, new_col, new_row):  # Return True if move was made, False if move was not possible
        # shift from algebraic notation to array notation
        init_row = init_row - 1

        if (init_row<0) or (init_row>7):
            return False 

        if (init_col not in self.colDict):
            print("Not a valid move, try again.")
            return False

        init_col = self.colDict[init_col]
        new_row = new_row - 1

        if (new_row<0) or (new_row>7):
            return False
        if (new_col not in self.colDict):
            return False
        new_col = self.colDict[new_col]

        # Move Piece

        piece = self.matrix[init_row][init_col]

        if (piece == 0):    # If user has selected an empty square
            return False

        legal_moves = piece.CheckMoves(self)
        print(legal_moves)

        if [new_row, new_col] not in legal_moves:
            return False
        else:   
            self.matrix[new_row][new_col] = piece
            self.matrix[piece.row][piece.col] = 0 
            piece.row = new_row
            piece.col = new_col
            piece.moves = [piece.row, piece.col]
            piece.image_height = 37+((635/8)*(7-piece.row))
            piece.image_width = 37+((634/8)*(piece.col))
            if (type(piece) == Pawn):
                piece.image_width = 35 + ((634/8)*(piece.col))
            return True

    def ResetBoard(self):
        self.pieces = [Rook(0,0,"white"), Knight(0,1,"white"), Bishop(0,2,"white"), Queen(0,3,"white"), King(0,4,"white"), Bishop(0,5,"white"), Knight(0,6,"white"), Rook(0,7,"white")]
        for i in range(0,8):
            self.pieces.append(Pawn(1,i,"white"))
        for i in range(0,8):
            self.pieces.append(Pawn(6,i,"black"))
        self.pieces = self.pieces + [Rook(7,0,"black"), Knight(7,1,"black"), Bishop(7,2,"black"), Queen(7,3,"black"), King(7,4,"black"), Bishop(7,5,"black"), Knight(7,6,"black"), Rook(7,7,"black")]
        self.matrix = []
        for i in range(0,8):
            self.matrix.append([0,0,0,0,0,0,0,0])
        for piece in self.pieces:
            self.matrix[piece.row][piece.col] = piece

    def Play(self):
        pygame.init()
        white = (255,255,255)
        image_width = 691       # Chessboard image is 691x691
        image_height = 850

        display_surface = pygame.display.set_mode((image_width,image_height))
        pygame.display.set_caption("Chess")
        board_image = pygame.image.load(r'C:\Users\jhlia\Desktop\chess\chessboard.jpg')

        input_box = pygame.Rect(0,691,691,159)  # Height of box is 850 - 691
        font = pygame.font.Font(None, 32)
        color_inactive = pygame.Color('darkolivegreen')
        color_active = pygame.Color('sienna')
        color = color_inactive
        active = False
        pre_text = 'Enter the square of the piece you want to move, and the square'
        pre_text_1 = 'you want to move it to (eg. E2 E4), or \"reset\" to start over:' 
        pre_txt_surface = font.render(pre_text, True, color)
        pre_txt_surface_1 = font.render(pre_text_1, True, color)
        text = ''

        running = True
        while running:
            for event in pygame.event.get():
                reset = False
                display_surface.fill(white)
                display_surface.blit(board_image, (0,0))
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True 
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            if (len(text) == 5):
                                if text == "reset":        
                                    reset = True
                                    text = 'Resetting...'
                                    txt_surface = font.render(text, True, color)
                                    display_surface.blit(txt_surface, (input_box.x+5, input_box.y+5))
                                    pygame.draw.rect(display_surface, color, input_box, 2)
                                    pygame.display.update()
                                    pygame.time.wait(2000)
                                    self.ResetBoard()
                                    for row in self.matrix:
                                        for tile in row:
                                            if tile != 0:
                                                display_surface.blit(tile.image, (tile.image_width, tile.image_height))
                                    pygame.display.update()
                                try: 
                                    result = self.MovePiece(text[0],int(text[1]),text[3],int(text[4]))
                                except ValueError:
                                    if reset != True:
                                        result = False
                                        text = 'Not a valid move, try again'
                                        txt_surface = font.render(text, True, color)
                                        display_surface.blit(txt_surface, (input_box.x+5, input_box.y+5))
                                        pygame.draw.rect(display_surface, color, input_box, 2)
                                        for row in self.matrix:
                                            for tile in row:
                                                if tile != 0:
                                                    display_surface.blit(tile.image, (tile.image_width, tile.image_height))
                                        pygame.display.update()
                                        pygame.time.wait(1000)
                                if result == False:
                                    if reset != True:
                                        text = 'Not a valid move, try again'
                                        txt_surface = font.render(text, True, color)
                                        display_surface.blit(txt_surface, (input_box.x+5, input_box.y+5))
                                        pygame.draw.rect(display_surface, color, input_box, 2)
                                        for row in self.matrix:
                                            for tile in row:
                                                if tile != 0:
                                                    display_surface.blit(tile.image, (tile.image_width, tile.image_height))
                                        pygame.display.update()
                                        pygame.time.wait(1000)
                            else:
                                if reset != True:
                                    text = 'Not a valid move, try again'
                                    txt_surface = font.render(text, True, color)
                                    display_surface.blit(txt_surface, (input_box.x+5, input_box.y+5))
                                    pygame.draw.rect(display_surface, color, input_box, 2)
                                    pygame.display.update()
                                    for row in self.matrix:
                                            for tile in row:
                                                if tile != 0:
                                                    display_surface.blit(tile.image, (tile.image_width, tile.image_height))
                                    pygame.display.update()
                                    pygame.time.wait(1000)
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                if reset != True:
                    txt_surface = font.render(text, True, color)
                    display_surface.blit(pre_txt_surface, (input_box.x+5, input_box.y + 5))
                    display_surface.blit(pre_txt_surface_1, (input_box.x+5, input_box.y + 45))
                    display_surface.blit(txt_surface, (input_box.x+5, input_box.y + 85))
                    pygame.draw.rect(display_surface, color, input_box, 2)

                    for row in self.matrix:
                        for tile in row:
                            if tile != 0:
                                display_surface.blit(tile.image, (tile.image_width, tile.image_height))
                    pygame.display.update()