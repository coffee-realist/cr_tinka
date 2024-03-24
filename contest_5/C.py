from bisect import bisect
import random


def is_prime(n):
    for c in range(2, int(n ** 0.5) + 1):
        if n % c == 0:
            return False
    return True


def prev_prime(x):
    while True:
        x -= 1
        if is_prime(x):
            return x


random.seed(0)
limits = 2 * 10 ** 9, 2 * 10 ** 9 + 10 ** 8
m_1 = prev_prime(random.randint(*limits))
m_2 = prev_prime(random.randint(*limits))
p = 79
a = input()
b = input()
la = len(a)
lb = len(b)
n = max(lb * 2, la)
pows_1 = [1 % m_1] + [0] * n
pows_2 = [1 % m_2] + [0] * n
for i in range(1, n + 1):
    pows_1[i] = (pows_1[i - 1] * p) % m_1
    pows_2[i] = (pows_2[i - 1] * p) % m_2
b_sum_1 = [0] * (lb * 2 + 1)
b_sum_2 = [0] * (lb * 2 + 1)
for i in range(1, lb * 2 + 1):
    b_sum_1[i] = (b_sum_1[i - 1] + ord(b[i % lb]) * pows_1[i - 1]) % m_1
    b_sum_2[i] = (b_sum_2[i - 1] + ord(b[i % lb]) * pows_2[i - 1]) % m_2
a_sum_1 = [0] * (la + 1)
a_sum_2 = [0] * (la + 1)
for i in range(1, la + 1):
    a_sum_1[i] = (a_sum_1[i - 1] + ord(a[i - 1]) * pows_1[i - 1]) % m_1
    a_sum_2[i] = (a_sum_2[i - 1] + ord(a[i - 1]) * pows_2[i - 1]) % m_2
shifts = []
for i in range(lb, lb * 2):
    r_1 = ((b_sum_1[i] - b_sum_1[i - lb] + m_1) * pows_1[n - i]) % m_1
    r_2 = ((b_sum_2[i] - b_sum_2[i - lb] + m_2) * pows_2[n - i]) % m_2
    shifts.append((r_1, r_2))
shifts.sort()
result = 0
for i in range(lb, la + 1):
    r_1 = ((a_sum_1[i] - a_sum_1[i - lb] + m_1) * pows_1[n - i]) % m_1
    r_2 = ((a_sum_2[i] - a_sum_2[i - lb] + m_2) * pows_2[n - i]) % m_2
    if bisect(shifts, (r_1, r_2)):
        result += 1
print(result)
