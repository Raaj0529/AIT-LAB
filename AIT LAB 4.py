def is_safe(row, col, queens, n):
    for r, c in queens:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True

def forward_check(row, col, domains, n):
    new_domains = [d.copy() for d in domains]
    for r in range(row + 1, n):
        if col in new_domains[r]:
            new_domains[r].remove(col)
        diag1 = col + (r - row)
        diag2 = col - (r - row)
        if diag1 in new_domains[r]:
            new_domains[r].remove(diag1)
        if diag2 in new_domains[r]:
            new_domains[r].remove(diag2)
        if len(new_domains[r]) == 0:
            return None
    return new_domains

def solve_nqueens(n):
    solutions = []

    def backtrack(row, queens, domains):
        if row == n:
            solutions.append(queens[:])
            return
        for col in domains[row]:
            if is_safe(row, col, queens, n):
                new_domains = forward_check(row, col, domains, n)
                if new_domains is not None:
                    queens.append((row, col))
                    backtrack(row + 1, queens, new_domains)
                    queens.pop()

    domains = [list(range(n)) for _ in range(n)]
    backtrack(0, [], domains)
    return solutions

n = 4
sol = solve_nqueens(n)
for s in sol:
    print(s)
