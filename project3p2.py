

def safe(row, column, board):
    for column in range(len(board)):
        if board[row][column] == 1:
            return False
    for r in range(row, 0, -1):
        for c in range(column, 0, -1):
            if board[r][c] == 1:
                return False
    for r in range(0, row):
        for c in range(column, 0, -1):
            if board[r][c] == 1:
                return False
    return True


def n_queen(n, nq, board):
    if n == nq:
        return True
    for row in range(len(board)):
        if safe(row, n, board):
            board[row][n] = 1
            if n_queen(n+1, nq, board):
                return True
            board[row][n] = 0
    return False


def main():
    nq = int(input("N-Queens Solver\nEnter a number to test:\n"))

    if nq <= 3:
        print("There are no solutions for boards of size 3 or less")
    elif 4 <= nq:
        board = [[0 for x in range(nq)] for x in range(nq)]
        result_nqueen = n_queen(0, nq, board)

    if result_nqueen:
        print(board)
    elif not result_nqueen:
        print("No Solution Found!")

if __name__ == "__main__":
    main()
