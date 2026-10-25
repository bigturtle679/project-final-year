import random

dist = [
    [0, 10, 15, 20, 25, 30],
    [10, 0, 35, 25, 20, 15],
    [15, 35, 0, 30, 10, 20],
    [20, 25, 30, 0, 15, 25],
    [25, 20, 10, 15, 0, 35],
    [30, 15, 20, 25, 35, 0]
]
n = 6
k = 2

def cost(path):
    return sum(dist[path[i]][path[i + 1]] for i in range(n - 1)) + dist[path[-1]][path[0]]

def neighbors(path):
    result = []
    for i in range(1, n):
        for j in range(i + 1, n):
            new = path[:]
            new[i], new[j] = new[j], new[i]
            result.append(tuple(new))
    return result

states = set()
while len(states) < k:
    tail = list(range(1, n))
    random.shuffle(tail)
    states.add(tuple([0] + tail))

visited = set(states)
best = min(states, key=cost)
for step in range(10):
    candidates = {route for state in states for route in neighbors(list(state)) if route not in visited}
    if not candidates:
        break
    visited.update(candidates)
    states = set(sorted(candidates, key=cost)[:k])
    step_best = min(states, key=cost)
    if cost(step_best) < cost(best):
        best = step_best
    print(f"\nStep {step + 1}")
    print("Route:", list(step_best) + [step_best[0]])
    print("Distance:", cost(step_best))

print("\n-------------------------")
print("Final Best Route:", list(best) + [best[0]])
print("Minimum Distance:", cost(best))
