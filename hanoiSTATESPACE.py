from collections import deque

def successors(state):
    result = []
    pegs = [list(peg) for peg in state]
    for source in range(3):
        if not pegs[source]:
            continue
        disk = pegs[source][-1]
        for destination in range(3):
            if source == destination or (pegs[destination] and pegs[destination][-1] < disk):
                continue
            next_pegs = [peg[:] for peg in pegs]
            next_pegs[source].pop()
            next_pegs[destination].append(disk)
            result.append((tuple(map(tuple, next_pegs)), (source, destination)))
    return result

def state_space_search(disks):
    start = (tuple(range(disks, 0, -1)), (), ())
    goal = ((), (), tuple(range(disks, 0, -1)))
    frontier = deque([start])
    parent = {start: (None, None)}
    depth = {start: 0}
    explored = 0
    current_level = -1
    level_count = 0

    while frontier:
        state = frontier.popleft()
        explored += 1
        level = depth[state]
        if level != current_level:
            if current_level != -1:
                print(f"Total states at Level {current_level}: {level_count}\n")
            current_level = level
            level_count = 0
            print(f"{'=' * 15} LEVEL {level} {'=' * 15}")
        print(state)
        level_count += 1
        if state == goal:
            break
        for next_state, action in successors(state):
            if next_state not in parent:
                parent[next_state] = (state, action)
                depth[next_state] = depth[state] + 1
                frontier.append(next_state)

    if current_level != -1:
        print(f"Total states at Level {current_level}: {level_count}")

    if goal not in parent:
        return None, explored

    path = []
    state = goal
    while parent[state][0] is not None:
        previous, action = parent[state]
        path.append(action)
        state = previous
    return path[::-1], explored

disks = int(input("Enter number of disks: "))
moves, explored = state_space_search(disks)
print("\nStates explored:", explored)
print("\n========== SHORTEST SOLUTION ==========")
if moves is None:
    print("No solution found.")
else:
    for number, (source, destination) in enumerate(moves, 1):
        print(f"Move {number}: Peg {source} -> Peg {destination}")
    print("Total moves:", len(moves))
