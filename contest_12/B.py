from collections import Counter

n = int(input())
divisors = []
i = 2
while i * i <= n:
    if n % i == 0:
        divisors.append(i)
        n //= i
    else:
        i += 1
if n > 1:
    divisors.append(n)
result = []
for divisor, cnt in Counter(divisors).items():
    result.append(f'{divisor}^{cnt}' if cnt > 1 else f'{divisor}')
print('*'.join(result))
