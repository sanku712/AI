def can_place(board, row, col):
    # Check if there's any queen in the same column or diagonal
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == row - r:
            return False
    return True

def print_solution(board):
    for row in board:
        print(' '.join('Q' if col == row else '-' for col in range(len(board))))
    print()

def solve_n_queens(n, row, board):
    if row == n:
        print_solution(board)
        return
    for col in range(n):
        if can_place(board, row, col):
            board[row] = col
            solve_n_queens(n, row + 1, board)

def n_queens(n):
    board = [-1] * n
    solve_n_queens(n, 0, board)

def main():
    print("****** N-Queens Solution ******")
    n = int(input("Enter the number of queens: "))
    n_queens(n)
if __name__ == "__main__":
    main()