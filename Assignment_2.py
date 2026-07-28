player, opponent = 'x', 'o'


def isMoveLeft(board):
    for row in board:
        if '_' in row:
            return True
    return False


def evaluate(board):
    
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '_':
            if row[0] == player:
                return 10
            elif row[0] == opponent:
                return -10

   
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '_':
            if board[0][col] == player:
                return 10
            elif board[0][col] == opponent:
                return -10

    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        if board[0][0] == player:
            return 10
        elif board[0][0] == opponent:
            return -10

   
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        if board[0][2] == player:
            return 10
        elif board[0][2] == opponent:
            return -10

    return 0


def minimax(board, depth, isMax):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not isMoveLeft(board):
        return 0

    if isMax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = player
                    best = max(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_' 
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_'
        return best


def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player
                moveVal = minimax(board, 0, False)
                board[i][j] = '_'

                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove


def printBoard(board):
    for row in board:
        print(" ".join(row))
    print()



def playGame():
    board = [['_', '_', '_'],
             ['_', '_', '_'],
             ['_', '_', '_']]

    turn = "human"  

    while True:
        printBoard(board)

        
        score = evaluate(board)
        if score == 10:
            print("X (Human) Wins!")
            break
        elif score == -10:
            print("O (Computer) Wins!")
            break
        elif not isMoveLeft(board):
            print("It's a Draw!")
            break

        if turn == "human":
            print("Your turn (X). Enter row and column (0-2):")
            r, c = map(int, input().split())
            if board[r][c] == '_':
                board[r][c] = 'x'
                turn = "computer"
            else:
                print("Invalid move! Try again.")
        else:
            print("Computer's turn (O)...")
            move = findBestMove(board)
            board[move[0]][move[1]] = 'o'
            turn = "human"



playGame()








# #output 
# hp@hp:~/B_17 NEW$ python3 ASSI2.py
# _ _ _
# _ _ _
# _ _ _

# Your turn (X). Enter row and column (0-2):
# 0 0 
# x _ _
# _ _ _
# _ _ _

# Computer's turn (O)...
# x o _
# _ _ _
# _ _ _

# Your turn (X). Enter row and column (0-2):
# 1 1 
# x o _
# _ x _
# _ _ _

# Computer's turn (O)...
# x o _
# _ x _
# _ _ o

# Your turn (X). Enter row and column (0-2):
# 2 0 
# x o _
# _ x _
# x _ o

# Computer's turn (O)...
# x o o
# _ x _
# x _ o

# Your turn (X). Enter row and column (0-2):
# 1 0 
# x o o
# x x _
# x _ o


# X (Human) Wins!
# */

