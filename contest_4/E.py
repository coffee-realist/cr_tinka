from math import inf


def get_k(x):
    sectors = 0
    current_sum = 0
    for i in lst:
        if i > x:
            return inf
        if current_sum + i <= x:
            current_sum += i
        else:
            sectors += 1
            current_sum = i
    return sectors + 1


n, k = map(int, input().split())
lst = list(map(int, input().split()))
left = min(lst)
right = int(2e14)
while right - left > 1:
    mid = (left + right) // 2
    current_k = get_k(mid)
    if current_k <= k:
        right = mid
    else:
        left = mid
if n == 1:
    print(left)
else:
    print(right)
