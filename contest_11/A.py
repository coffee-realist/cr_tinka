from sys import setrecursionlimit

setrecursionlimit(100000)


def find_path(cur):
    if cur == 0:
        return
    path.append(parents[cur])
    find_path(parents[cur])


def find_lca(cur, ind):
    if cur == -1:
        return 0
    while ind < k and path[ind] > cur:
        ind += 1
    if cur == path[ind]:
        return cur
    return find_lca(parents[cur], ind)


n = int(input())
lst = list(map(int, input().split()))
tree = dict()
parents = [-1] * n
for i in range(n - 1):
    try:
        tree[lst[i]].append(i + 1)
    except KeyError:
        tree[lst[i]] = [i + 1]
    parents[i + 1] = lst[i]
for _ in range(int(input())):
    u, v = map(int, input().split())
    path = [u]
    find_path(u)
    k = len(path)
    print(find_lca(v, 0))
