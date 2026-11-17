
def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def is_valid(board, num, pos):
    row, col = pos

    for j in range(9):
        if j != col and board[row][j] == num:
            return False

    for i in range(9):
        if i != row and board[i][col] == num:
            return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if (i, j) != pos and board[i][j] == num:
                return False

    return True


def solve(board):
    empty = find_empty(board)

    if empty is None:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


print("ENTER SUDOKU PUZZLE")
print("Enter 9 numbers in each row.")
print("Use 0 for empty cells.")

board = []

for i in range(9):
    while True:
        values = input(f"Enter row {i + 1}: ").split()

        if len(values) != 9:
            print("Please enter exactly 9 numbers.")
            continue

        if not all(v.isdigit() and 0 <= int(v) <= 9 for v in values):
            print("Enter numbers from 0 to 9 only.")
            continue

        board.append([int(v) for v in values])
        break

print("\nYOUR SUDOKU:")
print_board(board)

# Check original puzzle for duplicate numbers
valid = True
for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num != 0:
            board[i][j] = 0
            if not is_valid(board, num, (i, j)):
                valid = False
            board[i][j] = num

if valid and solve(board):
    print("\nSOLVED SUDOKU:")
    print_board(board)
else:
    print("\nInvalid puzzle or no solution exists.")
