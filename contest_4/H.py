n, c = map(int, input().split())
lst = []
for i in range(n):
    start, time = list(map(int, input().split()))
    lst.append([start, start + time, i + 1])
lst.sort(reverse=True)
result = c
start, end, ind = lst.pop()
problems = [ind]
while len(lst):
    current = lst.pop()
    if current[1] < end:
        problems.pop()
        start, end, ind = current
        problems.append(current[-1])
    elif current[0] >= end:
        start, end, ind = current
        problems.append(ind)
        result += c
print(result)
print(len(problems))
print(*problems)
