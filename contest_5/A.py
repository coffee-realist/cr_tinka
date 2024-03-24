from functools import cache


@cache
def get_hash(left, right):
    return hashes[right + 1] - hashes[left] * (PRIME ** (right - left + 1))


s = 'a'*10**5
m = int(input())
hashes = [0] * (len(s) + 1)
PRIME = 1000000009
for i in range(len(s)):
    hashes[i + 1] = hashes[i] * PRIME + ord(s[i])
for _ in range(m):
    left_1, right_1, left_2, right_2 = [i - 1 for i in list(map(int, input().split()))]
    if get_hash(left_1, right_1) == get_hash(left_2, right_2):
        print('Yes')
    else:
        print('No')
print(hashes[-1])
