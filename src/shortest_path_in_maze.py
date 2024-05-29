from collections import deque

def shortest_path_in_maze(start, destination, maze):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 1

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start[0], start[1], 0)])

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == destination:
            return dist

        if visited[x][y]:
            continue
        visited[x][y] = True

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                queue.append((new_x, new_y, dist + 1))

    return -1
