def f(x):
    return a * x * x * x + b * x * x + c * x + d


a, b, c, d = map(int, input().split())
eps = 0.000001
right = 1
while f(right) * f(-right) >= 0:
    right *= 2
left = -right
while right - left > eps:
    mid = (left + right) / 2
    if f(mid) * f(right) <= 0:
        left = mid
    else:
        right = mid
print(right)
