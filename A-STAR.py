from collections import deque

# Generate all valid next states
def get_next_states(state):
    states = []
    pegs = [list(p) for p in state]

    for i in range(3):
        if pegs[i]:  # Source peg is not empty
            disk = pegs[i][-1]

            for j in range(3):
                if i != j:
                    # Destination peg is empty or top disk is larger
                    if not pegs[j] or pegs[j][-1] > disk:
                        new_pegs = [p[:] for p in pegs]
                        new_pegs[i].pop()
                        new_pegs[j].append(disk)

                        states.append((tuple(map(tuple, new_pegs)), (i, j)))

    return states


def tower_of_hanoi_bfs(n):
    start = (tuple(range(n, 0, -1)), (), ())
    goal = ((), (), tuple(range(n, 0, -1)))

    queue = deque([(start, [], 0)])      # (state, path, level)
    visited = {start}

    current_level = -1
    level_count = 0
    solution = None

    while queue:
        state, path, level = queue.popleft()

        # Print level heading
        if level != current_level:
            if current_level != -1:
                print(f"\nTotal states at Level {current_level}: {level_count}")

            current_level = level
            level_count = 0
            print(f"\n{'='*15} LEVEL {level} {'='*15}")

        print(state)
        level_count += 1

        # Store solution but continue BFS
        if state == goal and solution is None:
            solution = path

        # Generate next states
        for new_state, move in get_next_states(state):
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [move], level + 1))

    print(f"\nTotal states at Level {current_level}: {level_count}")
    print("\nTotal Unique States Explored =", len(visited))

    return solution


# ---------------- MAIN PROGRAM ----------------

n = int(input("Enter number of disks: "))

moves = tower_of_hanoi_bfs(n)

print("\n========== SHORTEST SOLUTION ==========")

for i, (a, b) in enumerate(moves, 1):
    print(f"Move {i}: Peg {a} -> Peg {b}")

print("\nTotal Moves =", len(moves))