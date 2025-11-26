from collections import deque

def water_jug_problem(jug1, jug2, target):
    visited = set()
    queue = deque()
    queue.append((0, 0))
    visited.add((0, 0))
    path = {}

    while queue:
        x, y = queue.popleft()
        if x == target or y == target:
            result = []
            while (x, y) in path:
                result.append((x, y))
                x, y = path[(x, y)]
            result.append((x, y))
            return result[::-1]

        next_states = set()

        next_states.add((jug1, y))
        next_states.add((x, jug2))
        next_states.add((0, y))
        next_states.add((x, 0))

        pour = min(x, jug2 - y)
        next_states.add((x - pour, y + pour))

        pour = min(y, jug1 - x)
        next_states.add((x + pour, y - pour))

        for nx, ny in next_states:
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                path[(nx, ny)] = (x, y)
                queue.append((nx, ny))
    return None

jug1 = 4
jug2 = 3
target = 2

solution = water_jug_problem(jug1, jug2, target)
print("Steps:")
for step in solution:
    print(step)
