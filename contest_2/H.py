# не решена
n = int(input())
lst = list(map(int, input().split()))
prefix = [0]
stack = []
for i in lst:
    prefix.append(prefix[-1] + i)
for i in lst:
    if len(stack) == 0:
        stack.append((i, i))
        continue
    if stack[-1][0] <= i:
        stack.append((i, stack[-1][0]))
    else:
        if stack[-1][-1] < i:
            stack.append((i, stack[-1][-1]))
        else:
            stack.append((i, i))
print(stack)
'''
6
3 1 6 4 5 2

8
3 1 6 2 3 4 5 3

'''