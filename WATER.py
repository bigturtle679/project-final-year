def water_jug_dfs(capacity1, capacity2, target):
    visited = set()
    path = []
    actions = []

    def dfs(jug1, jug2):
        if (jug1, jug2) in visited:
            return False
        visited.add((jug1, jug2))
        path.append((jug1, jug2))
        if jug1 == target or jug2 == target:
            return True
        moves = [
            ((capacity1, jug2), "Fill Jug 1"),
            ((jug1, capacity2), "Fill Jug 2"),
            ((0, jug2), "Empty Jug 1"),
            ((jug1, 0), "Empty Jug 2"),
            (
                (max(0, jug1 - (capacity2 - jug2)),
                 min(capacity2, jug1 + jug2)),
                "Pour Jug 1 -> Jug 2"
            ),
            (
                (min(capacity1, jug1 + jug2),
                 max(0, jug2 - (capacity1 - jug1))),
                "Pour Jug 2 -> Jug 1"
            )
        ]
        for next_state, action in moves:
            if next_state == (jug1, jug2):
                continue
            actions.append(action)
            if dfs(next_state[0], next_state[1]):
                return True
            actions.pop()
        path.pop()
        return False
    
    if dfs(0, 0):
        return path, actions
    return [], []

def display_solution(solution, actions, capacity1, capacity2, target):
    print(f"Start: {solution[0]}")
    for i in range(1, len(solution)):
        jug1, jug2 = solution[i]
        print(f"Step {i}: {actions[i - 1]} -> ({jug1}, {jug2})")
capacity1 = 3
capacity2 = 5
target = 4
solution, actions = water_jug_dfs(
    capacity1,
    capacity2,
    target
)
if solution:
    display_solution(
        solution,
        actions,
        capacity1,
        capacity2,
        target
    )
else:
    print("\n" + "=" * 65)
    print("                 NO SOLUTION FOUND")
    print("=" * 65)
