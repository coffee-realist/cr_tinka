# не решена
def bin_search(left, right, _type):
    min_delta = 1e9
    min_mid = 1e9
    last_mid = -1
    answers = []
    while True:
        mid = (left + right + 1) // 2
        s_1, s_2 = f(_type, mid - 1)
        delta = s_2 - s_1
        if abs(delta) < abs(min_delta):
            min_delta = delta
            min_mid = mid
            answers = [min_mid]
        elif abs(delta) == abs(min_delta):
            answers.append(mid)
        if delta >= 0:
            left = mid
        else:
            right = mid
        if mid == last_mid:
            break
        last_mid = mid
    return _type, min(answers), min_delta


def f(t, x):
    if t == 'V':
        s_1 = ((1 + x) * x // 2 + ((m * (n - 1) + 1) + (m * (n - 1) + x)) * x // 2) * n // 2
    else:
        s_1 = (1 + m * x) * m * x // 2
    s_2 = (1 + n * m) * n * m // 2 - s_1
    return s_1, s_2


for query in range(int(input())):
    n, m = map(int, input().split())
    matrix = []
    last = 0
    for i in range(n):
        matrix.append([last + i + 1 for i in range(m)])
        last += m
    s_v, k_v, d_v = bin_search(1, m, 'V')
    s_h, k_h, d_h = bin_search(1, n, 'H')
    if abs(d_v) <= abs(d_h):
        print(s_v, k_v)
    else:
        print(s_h, k_h)
'''
5
1 3
4 7
1 10
3 3
3 5

'''
