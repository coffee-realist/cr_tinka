from collections import deque


def bfs(start, end):
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
             (1, 2), (1, -2), (-1, 2), (-1, -2)]
    visited = [[False] * (n + 1) for _ in range(n + 1)]
    prev = [[None] * (n + 1) for _ in range(n + 1)]
    d = deque([start])
    visited[start[0]][start[1]] = True
    while d:
        x, y = d.popleft()
        if (x, y) == end:
            path = []
            while (x, y) is not None:
                path.append((x, y))
                if prev[x][y] is not None:
                    x, y = prev[x][y]
                else:
                    break
            return path[::-1]
        for d_x, d_y in moves:
            cur_x = x + d_x
            cur_y = y + d_y
            if is_inside_board(cur_x, cur_y) and not visited[cur_x][cur_y]:
                visited[cur_x][cur_y] = True
                prev[cur_x][cur_y] = (x, y)
                d.append((cur_x, cur_y))
    return []


def is_inside_board(x, y):
    return 1 <= x <= n and 1 <= y <= n


n = int(input())
path = bfs(tuple(map(int, input().split())), tuple(map(int, input().split())))
print(len(path) - 1)
for x, y in path:
    print(x, y)
'''
5
1 1
3 2

'''
