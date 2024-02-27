n = int(input())
zeros = list(map(int, input().split()))
a = [0] * n
last_zero = n
s = 0
print(1, end=' ')
for zero_ind in zeros:
    a[zero_ind - 1] = 1
    if zero_ind == last_zero:
        d = last_zero
        for i in range(last_zero - 1, -1, -1):
            if a[i] == 0:
                d = last_zero - i - 1
                last_zero = i + 1
                break
        s -= d
    s += 1
    print(s + 1, end=" ")
