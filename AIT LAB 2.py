from collections import deque

goal = "123456780"

def get_neighbors(state):
    i = state.index("0")
    moves = []
    r, c = divmod(i, 3)
    if r > 0: moves.append(i - 3)
    if r < 2: moves.append(i + 3)
    if c > 0: moves.append(i - 1)
    if c < 2: moves.append(i + 1)
    neighbors = []
    for m in moves:
        s = list(state)
        s[i], s[m] = s[m], s[i]
        neighbors.append("".join(s))
    return neighbors

def bfs(start):
    queue = deque([start])
    visited = {start: None}
    while queue:
        curr = queue.popleft()
        if curr == goal:
            path = []
            while curr is not None:
                path.append(curr)
                curr = visited[curr]
            return path[::-1]
        for n in get_neighbors(curr):
            if n not in visited:
                visited[n] = curr
                queue.append(n)
    return None

def dfs(start):
    stack = [start]
    visited = {start: None}
    while stack:
        curr = stack.pop()
        if curr == goal:
            path = []
            while curr is not None:
                path.append(curr)
                curr = visited[curr]
            return path[::-1]
        for n in get_neighbors(curr):
            if n not in visited:
                visited[n] = curr
                stack.append(n)
    return None

start = "123450786"

print("BFS Solution:")
b = bfs(start)
if b:
    for s in b:
        print(s[:3], s[3:6], s[6:])

print("\nDFS Solution:")
d = dfs(start)
if d:
    for s in d:
        print(s[:3], s[3:6], s[6:])
