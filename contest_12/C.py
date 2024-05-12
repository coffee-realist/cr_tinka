def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


n = int(input())
for p in range(2, n):
    if is_prime(p) and is_prime(n - p):
        print(p, n - p)
        break
