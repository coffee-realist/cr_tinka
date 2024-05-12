def mod_exp(x, p):
    result = 1
    while p > 0:
        if p % 2 == 1:
            result = (result * x) % m
        x = (x * x) % m
        p >>= 1
    return result


n, k = map(int, input().split())
f = [1] * (n + 1)
m = 10 ** 9 + 7
for i in range(2, n + 1):
    f[i] = f[i - 1] * i % m
a, b, c = f[n], f[k], f[n - k]
inv_b = mod_exp(b, m - 2)
inv_c = mod_exp(c, m - 2)
print(a * inv_b % m * inv_c % m)
