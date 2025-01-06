from Chess_Piece_Classes import *

# Initialize the Chess Board
board = Board()
grid = board.makeBoard()
print(grid)

# Make piece dictionary
# pieces = dict(pawn_1='Pawn 1', pawn_2='Pawn 2', pawn_3='Pawn 3', pawn_4='Pawn 4', pawn_5='Pawn 5', pawn_6='Pawn 6', pawn_7='Pawn 7', pawn_8='Pawn 8', rook_1='Rook 1', rook_2='Rook 2', knight_1='Knight 1', knight_2='Knight 2', bishop_1='Bishop 1', bishop_2='Bishop 2', queen='Queen', king='King')
# print(pieces)

# Test Class Functionality
occupiedSpace = board.occupiedSpaces(grid)
print(occupiedSpace)

test1 = board.isOccupied(occupiedSpace, (0, 1))
test2 = board.isOccupied(occupiedSpace, (3, 4))
test3 = board.isOccupied(occupiedSpace, (4, 7))
test4 = board.isOccupied(occupiedSpace, (1, 0))
# print(test1)
# print(test2)
# print(test3)
# print(test4)

test1 = board.board2Grid('E7')
test2 = board.board2Grid('C1')
test3 = board.board2Grid('F7')
test4 = board.board2Grid('A5')
test5 = board.grid2Board(1,4)
test6 = board.grid2Board(7,2)
test7 = board.grid2Board(1,5)
test8 = board.grid2Board(3,0)
# print(test1 == (1, 4))
# print(test2 == (7, 2))
# print(test3 == (1, 5))
# print(test4 == (3, 0))
# print(test5 == 'E7')
# print(test6 == 'C1')
# print(test7 == 'F7')
# print(test8 == 'A5')


# print('If every result is True except for the second and third boolean, code is ready to run.')

##################### Begin Terminal Simulation Code ######################

# Prompt User to Select a Piece to Move
def userSelectPiece():
    while True:
        print("Options: 'Pawn 1', 'Pawn 2', 'Pawn 3', 'Pawn 4', 'Pawn 5', 'Pawn 6', 'Pawn 7', 'Pawn 8', 'Rook 1', 'Rook 2', 'Knight 1', 'Knight 2', 'Bishop 1', 'Bishop 2', 'Queen', 'King'")
        piece = input("Select which piece you would like to move: ")
        options = ['Pawn 1', 'Pawn 2', 'Pawn 3', 'Pawn 4', 'Pawn 5', 'Pawn 6', 'Pawn 7', 'Pawn 8', 'Rook 1', 'Rook 2', 'Knight 1', 'Knight 2', 'Bishop 1', 'Bishop 2', 'Queen', 'King']
        if piece in options: return piece
        else: print("Input does not match selection, please try again")

# Prompt User to Select Target Movement Location
def userSelectMove():
    while True:
        print("Select which location you would like to move this piece to")
        move = input("Options: 'E7', 'F2', etc.  ")
        return board.board2Grid(move)

def main():
    while True:
        piece = userSelectPiece()
        move = userSelectMove()
        print(piece)
        print(move)
        grid = board.refreshBoard()
        if board.isBlocked(grid, piece, move[0], move[1]):
            print('This piece is blocked and cannot move to this position')
        else: 
            board.movePiece(piece, move[0], move[1])
            print('Move Complete')
            print(board.refreshBoard())
        if input("Would you like to continue Y/N") == "N": break

# Main function call
#main()
######################### End Terminal Simulation Code #########################



######################### Begin Function Sandbox ######################### 

def relocate(name, move):
    
    pass

def size(list):
    n = 0
    for element in list:
        n += 1
    return n

def getPaths(position, path):
    firstPath = [position]
    secondPath = [position]
    if path[0] < 0: i = -1 
    else: i = 1
    if path[1] < 0: j = -1
    else: j = 1

    # Loop for first path
    for row in range(abs(path[1])):
        newPosition = (position[0], position[1]+j)
        firstPath += [newPosition]
    for col in range(abs(path[0])):
        newPosition = (newPosition[0]+i, newPosition[1])
        firstPath += [newPosition]

    # Loop for second path
    newPosition = position
    for row in range(abs(path[0])):
        newPosition = (newPosition[0]+i, newPosition[1])
        secondPath += [newPosition]
    for col in range(abs(path[1])):
        newPosition = (newPosition[0], newPosition[1]+j)
        secondPath += [newPosition]

    # Return both paths
    paths = [firstPath, secondPath]
    return paths

def bestMoves(position, path):
    # Need to define the Current Position and Target Destination Using the Path
    # Path gives the delta needed to get to the final position and the search expands out 1 space in all directions past the current position
    # Need to compare possible moves and check pieces in path
    blockedPos1 = []
    blockedPos2 = []
    grid = board.refreshBoard()
    paths = getPaths(position, path)
    print(paths)

    # Identify blocked positions along the path
    for pos in paths[0]:
        if pos in board.occupiedSpaces(grid):
            blockedPos1 += [pos]
    for pos in paths[1]:
        if pos in board.occupiedSpaces(grid):
            blockedPos2 += [pos]
    if size(blockedPos1) == 0: return paths[0][0]
    if size(blockedPos2) == 0: return paths[0][0]
    
    # Identify possible relocation spaces for pieces on either path.
    # This section also makes sure relocation spots are not on the path
    checkSpaces = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, -1), (1, -1), (-1, 0), (0, -1)]
    relocationSpace = set()
    print(blockedPos1)
    print(blockedPos2)
    for pos in blockedPos1:
        print(f'Checking position: {pos}')
        for space in checkSpaces:
            checkPos = (pos[0]+space[0], pos[1]+space[1])
            print(checkPos)
            if (checkPos in paths[0]) or (checkPos in board.occupiedSpaces(grid)) or (checkPos in paths[1]): continue
            elif checkPos[0] < 0 or checkPos[0] > 7 or checkPos[1] < 0 or checkPos[0] > 7: continue
            else: relocationSpace.add((grid[pos[0]][pos[1]], checkPos))

    for pos in blockedPos2:
        print(f'Checking position: {pos}')
        for space in checkSpaces:
            checkPos = (pos[0]+space[0], pos[1]+space[1])
            print(checkPos)
            if (checkPos in paths[1]) or (checkPos in board.occupiedSpaces(grid)) or (checkPos in paths[0]): continue
            elif checkPos[0] < 0 or checkPos[0] > 7 or checkPos[1] < 0 or checkPos[0] > 7: continue
            else: relocationSpace.add((grid[pos[0]][pos[1]], checkPos))
    print(f'These are the Pieces and the spaces they can be relocated to: {relocationSpace}')
    return relocationSpace

def bestPath(position, path):
    # We are supplied with helper functions bestMoves() and getPaths()
    # bestPath should analyze the amount of obstacles on each path 
    paths = getPaths(position, path)
    relocationMoves = bestMoves(position, path)
    relocInPath1 = []
    relocInPath2 = []
    relocInPaths = (relocInPath1, relocInPath2)
    moves = []
    moveCount1 = 0
    moveCount2 = 0
    i = 0
    values1 = []
    values2 = []
    for move in relocationMoves: moves += [move]
    for pos in paths[0]: values1 += [grid[pos[0]][pos[1]]]
    for pos in paths[1]: values2 += [grid[pos[0]][pos[1]]]
    for move in moves:
        if move[0] in values1: moveCount1 += 1; i += 1; relocInPath1 += (move[0], move[1])
        elif move[0] in values2: moveCount2 += 1; i += 1; relocInPath2 += (move[0], move[1])
        else: i += 1
    if moveCount1 >= moveCount2: selectedPath = 0
    else: selectedPath = 1
    previousLoc = (Pawn_1.x, Pawn_1.y)
    relocate(relocInPaths[selectedPath][0], relocInPaths[selectedPath][1])
    print(f'Moved {move[0]} to {move[1]} to clear knight path')
    checkPath = paths[selectedPath]
    
    #moveKnight(position, checkPath)
    relocate(relocInPaths[selectedPath][0], relocInPaths[selectedPath][1])

test10 = bestPath((0, 1), (2, -1))

######################### End Function Sandbox #########################



######################## Main Code ###########################
# def main():
#     while True:
#         piece = userSelectPiece()
#         move = userSelectMove()
#         pawn_1.move(move[0], move[1])
#         print('Move Complete')
#         print(board)
#     pass

# main()