n = int(input())
lst = list(map(int, input().split())) + [-1]
stack = []
streak = 1
destroyed = 0
for i in lst:
    if len(stack) == 0:
        stack.append(i)
        continue
    if i == stack[-1]:
        streak += 1
    elif streak > 2:
        destroyed += streak
        to_destroy = stack.pop()
        while len(stack) and stack[-1] == to_destroy:
            stack.pop()
        if len(stack) > 1 and stack[-1] == stack[-2]:
            streak = 2
        else:
            streak = 1
        if len(stack) and i == stack[-1]:
            streak += 1
    else:
        streak = 1
    stack.append(i)
print(destroyed)
'''
10
3 3 2 1 1 1 2 2 3 3
34
0 0 0 1 2 3 4 5 6 7 8 9 0 0 9 9 8 8 7 7 6 6 5 5 4 4 3 3 2 2 1 1 0 0
5
0 1 1 1 1 0 0 2
'''