MAX_STEPS = 120
states = []

def is_safe(board, row, col):
    return all(board[r][col] != 'Q' and abs(col - c) != row - r
               for r in range(row) for c in range(8) if board[r][c] == 'Q')

def save_state(board, action, row, col):
    if len(states) < MAX_STEPS:
        states.append((action, row + 1, col + 1, [r[:] for r in board]))

def solve(board, row):
    if row == 8:
        return True
    for col in range(8):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            save_state(board, "PLACE", row, col)
            if solve(board, row + 1):
                return True
            board[row][col] = '.'
            save_state(board, "BACKTRACK", row, col)
    return False

def display_states():
    for start in range(0, len(states), 4):
        group = states[start:start + 4]
        print("\n" + "=" * 100)
        for i, (action, row, col, _) in enumerate(group):
            print(f"STEP {start + i + 1}: {action} ({row},{col})", end="       ")
        print()
        print("-" * 100)
        for r in range(8):
            for _, _, _, board in group:
                print(" ".join(board[r]), end="     ")
            print()
        print("=" * 100)

board = [['.' for _ in range(8)] for _ in range(8)]
print("==============================================")
print("       8-QUEENS BACKTRACKING SEARCH")
print("==============================================")
print("\nQ = Queen")
print(". = Empty Position")
if solve(board, 0):
    print("\nSearch states:")
    display_states()
    print("\n\n==============================================")
    print("               FINAL SOLUTION")
    print("==============================================")
    for row in board:
        print(" ".join(row))
else:
    print("No solution exists.")
