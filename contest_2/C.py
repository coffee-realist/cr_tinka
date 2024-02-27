stack = []
operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
}
for i in input().strip().split():
    if i.isdigit():
        stack.append(int(i))
    else:
        _1 = stack.pop()
        _2 = stack.pop()
        stack.append(operations[i](_2, _1))
print(stack[-1])
