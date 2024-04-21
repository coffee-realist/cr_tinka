import random
from math import inf
# не заходит по времени на питоне, нужно писать на плюсах

# реализация структуры данных курево, но можно решить и иначе
# а потом в эту структуру нужно дописать метод, делающий функцию next
# при помощи редактирования функции поиска, сам поиск нам не нужен
# про реализацию данной структуры можно почитать в инете и код реализации аналогично
# найти там же, если влом реализовывать с нуля


class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(1, _max)
        self.left = None
        self.right = None


def right_rotate(v):
    v_left = v.cur_left
    v_left_right = v_left.cur_right
    v_left.cur_right = v
    v.cur_left = v_left_right
    return v_left


def left_rotate(v):
    v_right = v.cur_right
    v_right_left = v_right.cur_left
    v_right.cur_left = v
    v.cur_right = v_right_left
    return v_right


def add(root, key):
    if not root:
        return TreapNode(key)
    if root.key >= key:
        root.cur_left = add(root.cur_left, key)
        if root.priority < root.cur_left.priority:
            root = right_rotate(root)
    else:
        root.cur_right = add(root.cur_right, key)
        if root.priority < root.cur_right.priority:
            root = left_rotate(root)
    return root


def _next(root, key, min_ans):
    if not root or root.key == key:
        return root, min_ans
    elif root.key == key:
        return root
    if root.key < key:
        return _next(root.cur_right, key, min_ans)
    return _next(root.cur_left, key, root.key if key < root.key < min_ans else min_ans)


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
        r, result = _next(treap, n, inf)
        last_ans = r.key if r else result
        if last_ans < n or last_ans == inf:
            last_ans = -1
        print(last_ans)
    last_op = op
'''
6
+ 1
+ 3
+ 3
? 2
+ 1
? 4

6
+ 1
+ 3
+ 3
? 1
+ 1
? 4

6
+ 1
+ 3
+ 3
? 3
+ 1
? 4

7
+ 50
+ 30
+ 40
+ 70
+ 60
+ 80
? 65

'''
