import sys

sys.setrecursionlimit(100000000)


def build_heap(end, ind):
    left_ind = ind * 2 + 1
    right_ind = ind * 2 + 2
    max_ind = ind
    if left_ind < end and lst[left_ind] > lst[ind]:
        max_ind = left_ind
    if right_ind < end and lst[right_ind] > lst[max_ind]:
        max_ind = right_ind
    if max_ind != ind:
        lst[ind], lst[max_ind] = lst[max_ind], lst[ind]
        build_heap(end, max_ind)


def heap_sort():
    for i in range(n // 2 - 1, -1, -1):
        build_heap(n, i)
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        build_heap(i, 0)


n = int(input())
lst = list(map(int, input().split()))
heap_sort()
print(*lst)
