res = 0
n = int(input())
seconds_per_day = 60 * 60 * 24
seconds = [0 for i in range(seconds_per_day)]
for _ in range(n):
    opened_h, opened_m, opened_s, closed_h, closed_m, closed_s = map(int, input().split())
    opened = (opened_h * 60 + opened_m) * 60 + opened_s
    closed = (closed_h * 60 + closed_m) * 60 + closed_s
    if opened < closed:
        for i in range(opened, closed):
            seconds[i] += 1
    else:
        for i in range(opened, seconds_per_day):
            seconds[i] += 1
        for i in range(closed):
            seconds[i] += 1
print(seconds.count(n))
