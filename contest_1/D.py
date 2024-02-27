c = float(input())
left = -1
right = 10 ** 10
eps = 0.0000001
while right - left > eps:
    x = (left + right) / 2
    f = x * x + (x + 1) ** (1 / 2)
    if f < c:
        left = x
    else:
        right = x
print(right)
