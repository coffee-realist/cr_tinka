def get_cows_cnt(x):
    last = lst[0]
    cnt = 1
    for i in lst[1:]:
        if i - last >= x:
            last = i
            cnt += 1
    return cnt


n, k = map(int, input().split())
lst = list(map(int, input().split()))
left = 1
right = lst[-1]
while right - left > 1:
    mid = (left + right) // 2
    if get_cows_cnt(mid) < k:
        right = mid
    else:
        left = mid
print(left)
