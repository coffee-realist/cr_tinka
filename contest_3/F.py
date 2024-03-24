import random
from math import inf


class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(1, _max)
        self.left = None
        self.right = None


def right_rotate(v):
    v_left = v.left
    v_left_right = v_left.right
    v_left.right = v
    v.left = v_left_right
    return v_left


def left_rotate(v):
    v_right = v.right
    v_right_left = v_right.left
    v_right.left = v
    v.right = v_right_left
    return v_right


def add(root, key):
    if not root:
        return TreapNode(key)
    if root.key >= key:
        root.left = add(root.left, key)
        if root.priority < root.left.priority:
            root = right_rotate(root)
    else:
        root.right = add(root.right, key)
        if root.priority < root.right.priority:
            root = left_rotate(root)
    return root


def _next(root, key, min_ans):
    if not root or root.key == key:
        return root, min_ans
    elif root.key == key:
        return root
    if root.key < key:
        return _next(root.right, key, min_ans)
    return _next(root.left, key, root.key if key < root.key < min_ans else min_ans)


_max = 2 ** 64
last_op = '+'
last_ans = 0
m = 10 ** 9
random.seed(0)
treap = None
for _ in range(int(input())):
    op, n = input().split()
    n = int(n)
    if op == '+':
        if last_op == '+':
            treap = add(treap, n)
        else:
            treap = add(treap, (n + last_ans) % m)
    else:
        r, ans = _next(treap, n, inf)
        last_ans = r.key if r else ans
        if last_ans < n or last_ans == inf:
            last_ans = -1
        print(last_ans)
    last_op = op
