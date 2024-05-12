def mod_exp(x, p):
    result = 1
    while p > 0:
        if p % 2 == 1:
            result = (result * x) % mod
        x = (x * x) % mod
        p >>= 1
    return result


n, m, k, mod = map(int, input().split())
print((mod_exp(m, n) * mod_exp(k, mod - 2)) % mod)
