from math import inf
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)


def get_min(s, i, used, counter):
    global mn, result
    if s == n:
        if len(used) < mn:
            mn = len(used)
            result = used[:]
        return
    if s > n or i == len(lst):
        return
    get_min(s, i + 1, used, counter)
    if counter[i] > 0:
        used.append(lst[i])
        counter[i] -= 1
        get_min(s + lst[i], i, used, counter)
        used.pop()
        counter[i] += 1
    if counter[i] > 1:
        used.extend([lst[i], lst[i]])
        counter[i] -= 2
        get_min(s + 2 * lst[i], i, used, counter)
        used.pop()
        used.pop()
        counter[i] += 2


input = stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
cnt = [2] * len(lst)
mn = inf
result = []
get_min(0, 0, [], cnt)
if mn == inf:
    print(0 if sum(lst) * 2 >= n else -1)
else:
    print(mn)
    print(*sorted(result))
