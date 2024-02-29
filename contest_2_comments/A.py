# ! питон медленная особь, задачи, требующие быстродействие, следует отправлять на специальном компиляторе pypy3 !
# (либо писать на плюсах)
# стек, хранящий пары (кортежи) чисел, первое из которых само число, а второе - текущий минимум стека
class Stack:
    def __init__(self):
        self.lst = []

    def add(self, x):
        try:
            # засовываем новый элемент в конец и считаем минимум от предыдущего минимума и нового числа
            self.lst.append((x, min(x, self.lst[-1][1])))
        except IndexError:
            # если стек был пустым, то новое число и будет минимумом
            self.lst.append((x, x))

    def remove_last(self):
        self.lst.pop()

    def minimal(self):
        return self.lst[-1][1]


stack = Stack()
for _ in range(int(input())):
    operation = input()
    if operation == '3':
        print(stack.minimal())
    elif operation == '2':
        stack.remove_last()
    else:
        stack.add(int(operation.split()[1]))
