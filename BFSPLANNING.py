from collections import deque

start = (4, 1, 3,
         0, 2, 5,
         6, 7, 8)
goal = (1, 2, 3,
        4, 0, 5,
        6, 7, 8)

def moves(state):
    pos = state.index(0)
    r, c = divmod(pos, 3)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new = list(state)
            p = nr * 3 + nc
            new[pos], new[p] = new[p], new[pos]
            yield tuple(new)

def bfs():
    queue = deque([(start, 0)])
    parent = {start: None}
    levels = {}
    while queue:
        state, level = queue.popleft()
        levels.setdefault(level, []).append(state)
        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return levels, path[::-1]
        for new_state in moves(state):
            if new_state not in parent:
                parent[new_state] = state
                queue.append((new_state, level + 1))
    return levels, []

def print_level(level, states):
    print(f"\nLEVEL {level}")
    for row in range(3):
        for state in states:
            values = ["_" if x == 0 else str(x)
                      for x in state[row * 3:row * 3 + 3]]
            print(" ".join(values), end="     ")
        print()

levels, path = bfs()
print("========== 8-PUZZLE BFS ==========")
for level, states in levels.items():
    print_level(level, states)
print("\n========== GOAL STATE ==========")
for row in range(3):
    values = ["_" if x == 0 else str(x)
              for x in goal[row * 3:row * 3 + 3]]
    print(" ".join(values))
print("\nSolution:", " -> ".join(str(state) for state in path) if path else "No solution found")
print("Moves:", len(path) - 1 if path else "N/A")
