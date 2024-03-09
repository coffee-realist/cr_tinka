n = int(input())
lst = list(map(int, input().split()))
stack = []
max_sum = 0
for current in lst:
    if len(stack) == 0 or current > stack[-1][0]:
        stack.append([current, current])
    else:
        in_while = False
        flag = False
        while len(stack) and current < stack[-1][0]:
            flag = False
            in_while = True
            last = stack.pop()
            current_sum = last[0] * last[-1]
            if current_sum > max_sum:
                max_sum = current_sum
            if len(stack) and current < stack[-1][0]:
                stack[-1][-1] += last[-1]
                flag = True
        if not flag:
            if in_while:
                stack.append([current, last[-1] + current])
            else:
                to_add = stack.pop(-1)[-1]
                stack.append([current, to_add + current])
                curr = stack[-1][0] * stack[-1][-1]
                if curr > max_sum:
                    max_sum = curr
while len(stack):
    current_sum = -1
    while current_sum <= max_sum and len(stack):
        last = stack.pop()
        current_sum = last[0] * last[-1]
        if len(stack):
            stack[-1][-1] += last[-1]
    if current_sum > max_sum:
        max_sum = current_sum
print(max_sum)
