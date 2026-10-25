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

def bfs(max_level=3):
    queue = deque([(start, 0)])
    visited = {start}
    levels = {}
    while queue:
        state, level = queue.popleft()
        if level > max_level:
            break
        levels.setdefault(level, []).append(state)
        for new_state in moves(state):
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, level + 1))
    return levels

def print_level(level, states):
    print(f"\nLEVEL {level}")
    for row in range(3):
        for state in states:
            values = ["_" if x == 0 else str(x)
                      for x in state[row * 3:row * 3 + 3]]
            print(" ".join(values), end="     ")
        print()

levels = bfs(3)
print("========== 8-PUZZLE BFS ==========")
for level, states in levels.items():
    print_level(level, states)
print("\n========== GOAL STATE ==========")
for row in range(3):
    values = ["_" if x == 0 else str(x)
              for x in goal[row * 3:row * 3 + 3]]
    print(" ".join(values))
print("\nTotal Levels Displayed:", len(levels) - 1)
