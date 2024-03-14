def get_k_ordered(x):
    ind = 0
    row = 1
    col = n
    while row <= n and col > 0:
        if row * col < x:
            ind += col
            row += 1
            continue
        col -= 1
    return ind


n, k = map(int, input().split())
left = 0
right = int(2e10)
while right - left > 1:
    mid = (left + right) // 2
    if get_k_ordered(mid) < k:
        left = mid
    else:
        right = mid
print(left)
