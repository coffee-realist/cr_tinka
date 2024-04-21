def update(tree, idx, val):
    while idx <= n:
        tree[idx] += val
        idx += idx & -idx


def query(tree, idx):
    sum_val = 0
    while idx > 0:
        sum_val += tree[idx]
        idx -= idx & -idx
    return sum_val


def find():
    if n < 3:
        return 0
    compressed = {v: i + 1 for i, v in enumerate(sorted(set(lst)))}
    tree_1 = [0] * (n + 1)
    tree_2 = [0] * (n + 1)
    smaller_right = [0] * n
    for j in range(n - 1, -1, -1):
        idx = compressed[lst[j]]
        smaller_right[j] = query(tree_1, idx - 1)
        update(tree_1, idx, 1)
    result = 0
    for j in range(n):
        idx = compressed[lst[j]]
        greater_left = query(tree_2, n) - query(tree_2, idx)
        result += greater_left * smaller_right[j]
        update(tree_2, idx, 1)
    return result


n = int(input())
lst = list(map(int, input().split()))
print(find())
