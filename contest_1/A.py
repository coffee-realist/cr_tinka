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
    if lst[right] == x or lst[left] == x:
        print('YES')
    else:
        print('NO')
