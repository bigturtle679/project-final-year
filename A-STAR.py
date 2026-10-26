import heapq

start = (2, 8, 3, 1, 6, 4, 7, 0, 5)
goal = (1, 2, 3, 8, 0, 4, 7, 6, 5)
moves = {"Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1)}


def show(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()


def heuristic(state):
    return sum(abs(i // 3 - goal.index(tile) // 3) + abs(i % 3 - goal.index(tile) % 3)
               for i, tile in enumerate(state) if tile)


def neighbors(state):
    blank = state.index(0)
    row, col = divmod(blank, 3)
    for move, (dr, dc) in moves.items():
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            other = r * 3 + c
            new = list(state)
            new[blank], new[other] = new[other], new[blank]
            yield tuple(new), move


def a_star(start, goal):
    queue = [(heuristic(start), 0, start)]
    costs, parents = {start: 0}, {start: (None, None)}
    visited = set()
    while queue:
        _, cost, state = heapq.heappop(queue)
        if state in visited:
            continue
        visited.add(state)
        if state == goal:
            path = []
            while state is not None:
                previous, move = parents[state]
                path.append((state, move))
                state = previous
            return path[::-1], len(visited)
        for nxt, move in neighbors(state):
            new_cost = cost + 1
            if nxt not in costs or new_cost < costs[nxt]:
                costs[nxt] = new_cost
                parents[nxt] = (state, move)
                heapq.heappush(queue, (new_cost + heuristic(nxt), new_cost, nxt))
    return None, len(visited)


print("=" * 50, "\n        A* ALGORITHM - 8 PUZZLE\n", "=" * 50, sep="")
print("\nInitial State:")
show(start)
print("Goal State:")
show(goal)
print("Searching for optimal solution...\n")

solution, explored = a_star(start, goal)
if solution:
    print("=" * 50, "\n             SOLUTION\n", "=" * 50, sep="")
    print(f"\nTotal moves: {len(solution) - 1}\nStates explored: {explored}\n")
    for step, (state, move) in enumerate(solution):
        print(f"Step {step}: " + ("Initial State" if step == 0 else f"Move Blank {move}"))
        show(state)
else:
    print("No solution exists.")
