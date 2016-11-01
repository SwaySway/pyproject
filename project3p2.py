

def n_queen(n, row, column, board, state):
    if state:
        board[row][column] = 1

    elif not state:
        print("Something")

def under_attack(board):










nq = int(input("N-Queens Solver\nEnter a number to test:\n"))

if nq <= 3:
    print("There are no solutions for boards of size 3 or less")
elif 4 <= nq <=22:
    board = [[0 for x in range(n)] for x in range(n)]
    n_queen(nq, 0, 0, board, True)


