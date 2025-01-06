###################### Define class for the board behahvior #################################

class Board:
    def __init__(self):
        status = True
        self.pawn_1 = Pawn(1, 0, 1, 0, status)
        self.pawn_2 = Pawn(1, 1, 1, 1, status)
        self.pawn_3 = Pawn(1, 2, 1, 2, status)
        self.pawn_4 = Pawn(1, 3, 1, 3, status)
        self.pawn_5 = Pawn(1, 4, 1, 4, status)
        self.pawn_6 = Pawn(1, 5, 1, 5, status)
        self.pawn_7 = Pawn(1, 6, 1, 6, status)
        self.pawn_8 = Pawn(1, 7, 1, 7, status)
        self.rook_1 = Rook(0, 0, 0, 0, status)
        self.rook_2 = Rook(0, 7, 0, 7, status)
        self.knight_1 = Knight(0, 1, 0, 1, status)
        self.knight_2 = Knight(0, 6, 0, 6, status)
        self.bishop_1 = Bishop(0, 2, 0, 2, status)
        self.bishop_2 = Bishop(0, 5, 0, 5, status)
        self.queen = Queen(0, 3, 0, 3, status)
        self.king = King(0, 4, 0, 4, status)
        self.piece = Piece(status)
        self.pieces = [self.pawn_1, self.pawn_2, self.pawn_3, self.pawn_4, self.pawn_5, self.pawn_6, self.pawn_7, self.pawn_8, self.rook_1, self.rook_2, self.knight_1, self.knight_2, self.bishop_1, self.bishop_2, self.queen, self.king]
        self.pieceNames = ['Pawn 1', 'Pawn 2', 'Pawn 3', 'Pawn 4', 'Pawn 5', 'Pawn 6', 'Pawn 7', 'Pawn 8', 'Rook 1', 'Rook 2', 'Knight 1', 'Knight 2', 'Bishop 1', 'Bishop 2', 'Queen', 'King']
        self.board = [[0 for col in range(8)] for row in range(8)]

    def makeBoard(self):
        # Assign piece positions
        self.board[self.pawn_1.homeX][self.pawn_1.homeY] = "Pawn 1"
        self.board[self.pawn_2.homeX][self.pawn_2.homeY] = "Pawn 2"
        self.board[self.pawn_3.homeX][self.pawn_3.homeY] = "Pawn 3"
        self.board[self.pawn_4.homeX][self.pawn_4.homeY] = "Pawn 4"
        self.board[self.pawn_5.homeX][self.pawn_5.homeY] = "Pawn 5"
        self.board[self.pawn_6.homeX][self.pawn_6.homeY] = "Pawn 6"
        self.board[self.pawn_7.homeX][self.pawn_7.homeY] = "Pawn 7"
        self.board[self.pawn_8.homeX][self.pawn_8.homeY] = "Pawn 8"
        self.board[self.rook_1.homeX][self.rook_1.homeY] = "Rook 1"
        self.board[self.rook_2.homeX][self.rook_2.homeY] = "Rook 2"
        self.board[self.knight_1.homeX][self.knight_1.homeY] = "Knight 1"
        self.board[self.knight_2.homeX][self.knight_2.homeY] = "Knight 2"
        self.board[self.bishop_1.homeX][self.bishop_1.homeY] = "Bishop 1"
        self.board[self.bishop_2.homeX][self.bishop_2.homeY] = "Bishop 2"
        self.board[self.queen.homeX][self.queen.homeY] = "Queen"
        self.board[self.king.homeX][self.king.homeY] = "King"
        return self.board
    
    def occupiedSpaces(self, board):
        i = 0
        j = 0
        spaces = []
        for row in board:
            for col in board[i]:
                if col != 0: spaces += [(i, j)]
                j += 1
            i += 1
            j = 0
        return spaces
    
    def isOccupied(self, occupiedSpaces, move):
        if type(move) == str: move  = self.board2Grid(self, move)
        if move in occupiedSpaces: return True
        else: return False
        
    def grid2Board(self, i, j):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        number = 8 - i
        letter = letters[j]
        return f'{letter}'+f'{number}'

    def board2Grid(self, name):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        letter = name[0]
        number = int(name[1])
        index = letters.index(letter)
        move = (8 - (number), index)
        return move

    def movePiece(self, name, moveX, moveY):
        if name in self.pieceNames:
            i = self.pieceNames.index(name)
            piece = self.pieces[i]
            piece.move(moveX, moveY)
        pass

    def isBlocked(self, grid, name, moveX, moveY):
        print(moveX, moveY)
        if name in self.pieceNames:
            i = self.pieceNames.index(name)
            checkPiece = self.pieces[i]
            path = checkPiece.piece.getPath(checkPiece.x, checkPiece.y, moveX, moveY)
        occupiedSpace = []
        for i in range(abs(path[0])+1):
            for j in range(abs(path[1])+1):
                if path[0] < 0 and path[1] <= 0: loc = grid[checkPiece.x - i][checkPiece.y - j]
                elif path[0] < 0 and path[1] >= 0: loc = grid[checkPiece.x - i][checkPiece.y + j]
                elif path[0] > 0 and path[1] <= 0: loc = grid[checkPiece.x + i][checkPiece.y - j]
                else: loc = grid[checkPiece.x + i][checkPiece.y + j]
                print(loc)
                if loc != 0:
                    occupiedSpace += [(checkPiece.x+i, checkPiece.y+j)]
        if (checkPiece.prevPos) in occupiedSpace:
            value = occupiedSpace.pop(0)
        if occupiedSpace == []: return False
        else: return True

    def refreshBoard(self):
        self.board[self.pawn_1.prevPos[0]][self.pawn_1.prevPos[1]] = 0
        self.board[self.pawn_2.prevPos[0]][self.pawn_2.prevPos[1]] = 0
        self.board[self.pawn_3.prevPos[0]][self.pawn_3.prevPos[1]] = 0
        self.board[self.pawn_4.prevPos[0]][self.pawn_4.prevPos[1]] = 0
        self.board[self.pawn_5.prevPos[0]][self.pawn_5.prevPos[1]] = 0
        self.board[self.pawn_6.prevPos[0]][self.pawn_6.prevPos[1]] = 0
        self.board[self.pawn_7.prevPos[0]][self.pawn_7.prevPos[1]] = 0
        self.board[self.pawn_8.prevPos[0]][self.pawn_8.prevPos[1]] = 0
        self.board[self.rook_1.prevPos[0]][self.rook_1.prevPos[1]] = 0
        self.board[self.rook_2.prevPos[0]][self.rook_2.prevPos[1]] = 0
        self.board[self.knight_1.prevPos[0]][self.knight_1.prevPos[1]] = 0
        self.board[self.knight_2.prevPos[0]][self.knight_2.prevPos[1]] = 0
        self.board[self.bishop_1.prevPos[0]][self.bishop_1.prevPos[1]] = 0
        self.board[self.bishop_2.prevPos[0]][self.bishop_2.prevPos[1]] = 0
        self.board[self.queen.prevPos[0]][self.queen.prevPos[1]] = 0
        self.board[self.king.prevPos[0]][self.king.prevPos[1]] = 0
        self.board[self.pawn_1.x][self.pawn_1.y] = "Pawn 1"
        self.board[self.pawn_2.x][self.pawn_2.y] = "Pawn 2"
        self.board[self.pawn_3.x][self.pawn_3.y] = "Pawn 3"
        self.board[self.pawn_4.x][self.pawn_4.y] = "Pawn 4"
        self.board[self.pawn_5.x][self.pawn_5.y] = "Pawn 5"
        self.board[self.pawn_6.x][self.pawn_6.y] = "Pawn 6"
        self.board[self.pawn_7.x][self.pawn_7.y] = "Pawn 7"
        self.board[self.pawn_8.x][self.pawn_8.y] = "Pawn 8"
        self.board[self.rook_1.x][self.rook_1.y] = "Rook 1"
        self.board[self.rook_2.x][self.rook_2.y] = "Rook 2"
        self.board[self.knight_1.x][self.knight_1.y] = "Knight 1"
        self.board[self.knight_2.x][self.knight_2.y] = "Knight 2"
        self.board[self.bishop_1.x][self.bishop_1.y] = "Bishop 1"
        self.board[self.bishop_2.x][self.bishop_2.y] = "Bishop 2"
        self.board[self.queen.x][self.queen.y] = "Queen"
        self.board[self.king.x][self.king.y] = "King"
        return self.board

######################## Define class to handle general piece behavior and attributes ############################

class Piece:
    def __init__(self, status):
        self.status = True
        
    # Returns if the piece is currently Active on the board
    def isActive(self):
        if self.status: return True
        else: return 
            
    def getPath(self, x, y, moveX, moveY):
        deltaX = moveX - x
        deltaY = moveY - y
        return (deltaX, deltaY)
    
    # Sets a pieces status to captured
    def captured(self):
        self.status = False
        return self.status

######################## Define classes for each piece #######################################

class Pawn:
    def __init__(self, x, y, homeX, homeY, status):
        self.x = x
        self.y = y
        self.homeX = homeX
        self.homeY = homeY
        self.position = (x, y)
        self.home = (homeX, homeY)
        self.status = status
        self.piece = Piece(self.status)
        self.prevPos = (homeX, homeY)

    def isLegalMove(self, moveX, moveY):
        currX, currY = self.homeX, self.homeY
        if not self.piece.isActive(): return False
        if ((self.home != self.position)):
            if (moveX - currX != 1) and (moveY - currY != 0): return False
            else: return True
        else:
            if ((moveX - currX == 2) or (moveX - currX == 1)) and (moveY - currY == 0): return True
            else: return False

    def move(self, moveX, moveY):
        currPos = self.position
        newPos = (moveX, moveY)
        if (self.isLegalMove(moveX, moveY)):
            self.prevPos = currPos
            currPos = newPos
            print(f'Pawn is now located at {currPos} with {(currPos[0] - self.prevPos[0], currPos[1] - self.prevPos[1])} spaces traversed')
        else:
            print(f'Pawn cannot locate to {newPos}. The move is illegal')
        (self.x, self.y) = currPos

class Rook:
    def __init__(self, x, y, homeX, homeY, status):
        self.x = x
        self.y = y
        self.homeX = homeX
        self.homeY = homeY
        self.position = (x, y)
        self.home = (homeX, homeY)
        self.status = status
        self.piece = Piece(status)
        self.prevPos = (homeX, homeY)
    
    def isLegalMove(self, moveX, moveY):
        currX, currY = self.x, self.y
        newX = self.x + moveX
        newY = self.y + moveY
        if not self.piece.isActive(): return False
        if (newX - currX != 0) and (newY - currY != 0): return False
        else: return True

    def move(self, moveX, moveY):
        currPos = self.position
        newPos = (moveX, moveY)
        if (self.isLegalMove(moveX, moveY)):
            self.prevPos = currPos
            currPos = newPos
            print(f'Rook is now located at {currPos} with {(currPos[0] - self.prevPos[0], currPos[1] - self.prevPos[1])} spaces traversed')
        else:
            print(f'Rook cannot locate to {newPos}. The move is illegal')
        (self.x, self.y) = currPos
    
class Knight:
    def __init__(self, x, y, homeX, homeY, status):
        self.x = x
        self.y = y
        self.homeX = homeX
        self.homeY = homeY
        self.position = (x, y)
        self.home = (homeX, homeY)
        self.status = status
        self.piece = Piece(status)
        self.prevPos = (homeX, homeY)

    def isLegalMove(self, moveX, moveY):
        currX, currY = self.x, self.y
        if not self.piece.isActive(): return False
        if (abs(moveX - currX) == 1) and (abs(moveY - currY) == 2): return True
        elif (abs(moveX - currX) == 2) and (abs(moveY - currY) == 1): return True
        else: return False

    def move(self, moveX, moveY):
        currPos = self.position
        newPos = (moveX, moveY)
        if (self.isLegalMove(moveX, moveY)):
            self.prevPos = currPos
            currPos = newPos
            print(f'Knight is now located at {currPos} with {(currPos[0] - self.prevPos[0], currPos[1] - self.prevPos[1])} spaces traversed')
        else:
            print(f'Knight cannot locate to {newPos}. The move is illegal')
        (self.x, self.y) = currPos
    
class Bishop:
    def __init__(self, x, y, homeX, homeY, status):
        self.x = x
        self.y = y
        self.homeX = homeX
        self.homeY = homeY
        self.position = (x, y)
        self.home = (homeX, homeY)
        self.status = status
        self.piece = Piece(status)
        self.prevPos = (homeX, homeY)
    
    def isLegalMove(self, moveX, moveY):
        currY, currX = self.x, self.y
        newX = moveX
        newY = moveY
        print((currX, currY))
        print((newX, newY))
        if not self.piece.isActive(): return False
        if (abs(newX - currX) != abs(newY - currY)): return False
        else: return True

    def move(self, moveX, moveY):
        currPos = self.position
        newPos = (moveX, moveY)
        if (self.isLegalMove(moveX, moveY)):
            self.prevPos = currPos
            currPos = newPos
            print(f'Bishop is now located at {(currPos[0] - self.prevPos[0], currPos[1] - self.prevPos[1])} spaces traversed')
        else:
            print(f'Bishop cannot locate to {newPos}. The move is illegal')
        (self.x, self.y) = currPos
    
class Queen:
    def __init__(self, x, y, homeX, homeY, status):
        self.x = x
        self.y = y
        self.homeX = homeX
        self.homeY = homeY
        self.position = (x, y)
        self.home = (homeX, homeY)
        self.status = status
        self.piece = Piece(status)
        self.prevPos = (homeX, homeY)
    
    def isLegalMove(self, moveX, moveY):
        currX, currY = self.x, self.y
        newX = self.x + moveX
        newY = self.y + moveY
        if not self.piece.isActive(): return False
        if (abs(newX - currX) == abs(newY - currY)): return True
        elif (newX - currX == 0) or (newY - currY == 0): return True
        else: return False

    def move(self, moveX, moveY):
        currPos = self.position
        newPos = (moveX, moveY)
        if (self.isLegalMove(moveX, moveY)):
            self.prevPos = currPos
            currPos = newPos
            print(f'Queen is now located at {currPos} with {(currPos[0] - self.prevPos[0], currPos[1] - self.prevPos[1])} spaces traversed')
        else:
            print(f'Queen cannot locate to {newPos}. The move is illegal')
        (self.x, self.y) = currPos
    
class King:
    def __init__(self, x, y, homeX, homeY, status):
        self.x = x
        self.y = y
        self.homeX = homeX
        self.homeY = homeY
        self.position = (x, y)
        self.home = (homeX, homeY)
        self.status = status
        self.piece = Piece(status)
        self.prevPos = (homeX, homeY)
    
    def isLegalMove(self, moveX, moveY):
        currX, currY = self.x, self.y
        newX = self.x + moveX
        newY = self.y + moveY
        if not self.piece.isActive(): return False
        if ((abs(newX - currX) == 1) and (abs(newY - currY) == 1)): return True
        elif (newX - currX == 1 and newY - currY == 0) or (newX - currX == 0 and newY - currY == 1): return True
        else: return False

    def move(self, moveX, moveY):
        currPos = self.position
        newPos = (moveX, moveY)
        if (self.isLegalMove(moveX, moveY)):
            self.prevPos = currPos
            currPos = newPos
            print(f'King is now located at {currPos} with {(currPos[0] - self.prevPos[0], currPos[1] - self.prevPos[1])} spaces traversed')
        else:
            print(f'King cannot locate to {newPos}. The move is illegal')
        (self.x, self.y) = currPos