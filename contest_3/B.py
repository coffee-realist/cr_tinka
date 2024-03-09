from sys import setrecursionlimit

setrecursionlimit(1000000)


def height(ind):
    try:
        root = tree[ind]
        if root == -1:
            return 0
        left_ind = ind * 2 + 1
        right_ind = ind * 2 + 2
    except IndexError:
        return 0
    left_height = height(left_ind)
    right_height = height(right_ind)
    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1


def check(ind, mxs, mns):
    try:
        root = tree[ind]
        if root == -1:
            return True
        left_ind = ind * 2 + 1
        right_ind = ind * 2 + 2
    except IndexError:
        return True
    left_height = height(left_ind)
    right_height = height(right_ind)
    if abs(left_height - right_height) > 1:
        return False
    for mx in mxs:
        if root > mx:
            return False
    for mn in mns:
        if root < mn:
            return False
    left_check = check(left_ind, mxs + [root], mns)
    right_check = check(right_ind, mxs, mns + [root])
    if left_check and right_check:
        return True


def build_tree(v, ind):
    global tree
    try:
        left, right = lst[v]
        tree[ind * 2 + 1] = left
        tree[ind * 2 + 2] = right
    except IndexError:
        return
    build_tree(left, ind * 2 + 1)
    build_tree(right, ind * 2 + 2)


n, r = map(int, input().split())
tree = [r] + [-1] * (n + 1) * 2
lst = []
for i in range(n):
    cur = list(map(int, input().split()))
    lst.append(cur)
build_tree(r, 0)
if check(0, [], []):
    print(1)
else:
    print(0)
