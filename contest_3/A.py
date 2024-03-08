import sys

sys.setrecursionlimit(900000)


def find_diameter(root):
    result = 1

    def dfs(k):
        nonlocal result
        children = [0, 0]
        lst = [dfs(child) for child in tree[k][1]]
        if len(lst):
            children = lst
        result = max(result, sum(sorted(children)[-2:]) + 1)
        return max(children) + 1

    dfs(root)
    return result - 1


n = int(input())
parents = list(map(int, input().split()))
tree = {0: [0, []]}
for i in range(len(parents)):
    tree[parents[i]][-1].append(i + 1)
    tree[i + 1] = [tree[parents[i]][0] + 1, []]
ans = []
for v in sorted(tree.keys()):
    ans.append(tree[v][0])
print(max(ans), find_diameter(0))
print(*ans)
