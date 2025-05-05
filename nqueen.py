def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True 

def solve_n_queens(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = 0  # Backtrack

    return False

def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))

def main():
    n = int(input("Enter the value of n (number of queens): "))
    board = [[0 for _ in range(n)] for _ in range(n)]
    print_board(board)

    if solve_n_queens(board, 0, n):
        print("\nOne of the solutions:")
        print_board(board)
    else:
        print("No solution exists for n =", n)

if __name__ == "__main__":
    main()
