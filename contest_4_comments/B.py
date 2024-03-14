n, m, k = map(int, input().split())
# аналогичная задача, только нужно искать префиксные суммы в матрице
# тут объяснять по коду довольно сложно, проще нарисовать матрицу на листочке,
# посчитать для нее отдельно матрицу префиксных сумм и
# осознать суммы каких прямоугольников нам нужно отнимать друг от друга, что происходит в последнем цикле
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
ps = [[0 for _ in range(m)] for __ in range(n)]
ps[0][0] = lst[0][0]
for i in range(1, m):
    ps[0][i] = ps[0][i - 1] + lst[0][i]
for i in range(1, n):
    ps[i][0] = ps[i - 1][0] + lst[i][0]
for i in range(1, n):
    for j in range(1, m):
        ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + lst[i][j]
for _ in range(k):
    y_1, x_1, y_2, x_2 = map(int, input().split())
    a = ps[y_2 - 1][x_2 - 1]
    b = ps[y_2 - 1][x_1 - 2] if x_1 > 1 else 0
    c = ps[y_1 - 2][x_2 - 1] if y_1 > 1 else 0
    d = ps[y_1 - 2][x_1 - 2] if y_1 > 1 and x_1 > 1 else 0
    print(a - b - c + d)
