# красиво решается на питоне словариком из лямбда функций
# можно решить и без выпендривания, но подлиньше
# задача довольно простая, нужно просто класть числа в стек, а как только находим операцию, то извлекать из стека
# последние два числа, проводить с ними эту операцию и результат класть в стек
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
