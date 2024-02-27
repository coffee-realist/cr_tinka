import sys


def query(x):
    print(x)
    sys.stdout.flush()
    return input()


n = int(input())
left = 1
right = n
mid = (left + right) // 2
while right != left:
    ans = query(mid)
    if ans == '<':
        right = mid - 1
        mid = (left + right) // 2 + 1
    elif ans == '>=':
        left = mid
        mid = (left + right) // 2 + 1
print(f'! {left}')
