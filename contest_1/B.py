n, k = map(int, input().split())
lst = list(map(int, input().split()))
to_find = list(map(int, input().split()))
for x in to_find:
    left = 0
    right = n - 1
    while right - left > 1:
        mid = (left + right) // 2
        if lst[mid] < x:
            left = mid
        else:
            right = mid
    if abs(lst[left] - x) <= abs(lst[right] - x):
        print(lst[left])
    else:
        print(lst[right])
