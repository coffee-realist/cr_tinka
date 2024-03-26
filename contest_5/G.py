import sys
import random


def lcs():
    mx = min(n, m)
    while mx > 0:
        for ind in range(n - mx + 1):
            for j in range(m - mx + 1):
                if (lst_1[n - ind] + lst_2[m - mx - j]) == (
                        lst_2[m - j] + lst_1[n - mx - ind]):
                    return mx
        mx -= 1
    return mx


def get_hash():
    return random.randint(1, sys.maxsize)


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
hashes = {a[0]: get_hash()}
lst_1 = [0] * (n + 1)
lst_1[1] = hashes[a[0]]
lst_2 = [0] * (m + 1)
for i in range(2, n + 1):
    cur = a[i - 1]
    if cur not in hashes:
        hashes[cur] = get_hash()
    lst_1[i] = lst_1[i - 1] + hashes[cur]
if b[0] not in hashes:
    hashes[b[0]] = get_hash()
lst_2[1] = hashes[b[0]]
for i in range(2, m + 1):
    cur = b[i - 1]
    if cur not in hashes:
        hashes[cur] = get_hash()
    lst_2[i] = lst_2[i - 1] + hashes[cur]
print(lcs())
