# [
# [X,X,O],
# [X,O,O],
# [O,X,X]
# ]

def isOver(board):
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]):
            return True
        elif (board[0][i] == board[1][i]== board[2][i]):
            return True
    if (board[0][0] == board[1][1] == board[2][2]):
            return True
    elif (board[0][2]  == board[1][1] == board[2][0]):
        return True
    return False

player1 = input("Jogador 1: ")
player2 = input("Jogador 2: ")

board = [[1,1,1],[1,1,1],[1,1,1]]
for i in range(3):
    for j in range(3):
        board[i][j] = False


running = True


while (running):
    print("Turno do jogador 1!")
    jogada1_linha = int(input("Escolha a linha "))
    jogada1_coluna = int(input("Escolhe a coluna "))
    if (board[jogada1_linha][jogada1_coluna] == False):
        board[jogada1_linha][jogada1_coluna] = "X"
        print(board)
    else:
        print("Jogada inválida")
    
    print("Turno do jogador 2!")
    jogada1_linha = int(input("Escolha a linha "))
    jogada1_coluna = int(input("Escolhe a coluna "))
    if (board[jogada1_linha][jogada1_coluna] == False):
        board[jogada1_linha][jogada1_coluna] = "O"
    else:
        print("Jogada inválida")
        print(board)

    if (isOver(board) == True):
        print("Game Over!")
        print(board)
        running = False
    