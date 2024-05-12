n = int(input())
if n == 0:
    print(1)
    quit()
x, cnt_2, cnt_5, result = n, 0, 0, 1
for i in range(2, n + 1):
    cur = i
    while cur % 2 == 0:
        cnt_2 += 1
        cur //= 2
    while cur % 5 == 0:
        cnt_5 += 1
        cur //= 5
    result = (result * (cur % 10)) % 10
for _ in range(cnt_2 - cnt_5):
    result = (result * 2) % 10
print(result)
