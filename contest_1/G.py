n = int(input())
lst = [i + 1 for i in range(n)]
j = 0
while j < n:
    lst[j], lst[j // 2] = lst[j // 2], lst[j]
    j += 1
print(*lst)
