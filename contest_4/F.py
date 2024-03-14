n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
lst.sort(reverse=True)
left, right = lst.pop()
result = right - left
while len(lst):
    if len(lst):
        current = lst.pop()
        while len(lst) and current[-1] <= right:
            current = lst.pop()
        if current[-1] > right:
            if current[0] < right:
                left = right
                right = current[-1]
            else:
                left, right = current
            result += right - left
print(result)
