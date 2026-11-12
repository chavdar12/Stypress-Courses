# Iterative maze path search (no recursion), using a list as the stack.
# 1 = wall, 0 = free, 7 = target, 3 = visited / potentially good, 5 = dead end
WALL, FREE, TARGET, GOOD, BAD = 1, 0, 7, 3, 5
SYMBOLS = {WALL: "#", FREE: " ", TARGET: "X", GOOD: ".", BAD: "~"}


def find_path(maze, start):
    stack = [start]
    while stack:
        row, col = stack[-1]
        if maze[row][col] == TARGET:
            return True
        if maze[row][col] == FREE:
            maze[row][col] = GOOD
        for r, c in ((row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)):
            if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] in (FREE, TARGET):
                stack.append((r, c))
                break
        else:  # no way forward: mark as dead end and step back
            maze[row][col] = BAD
            stack.pop()
    return False


def show(maze):
    for row in maze:
        print("".join(SYMBOLS[cell] for cell in row))


MAZE = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 1, 7, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

maze = [row[:] for row in MAZE]
assert find_path(maze, (1, 1))
blocked = [[1, 1, 1], [1, 0, 1], [1, 1, 7]]
assert not find_path(blocked, (1, 1))

if __name__ == "__main__":
    show(maze)
