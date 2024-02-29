class Stack:
    def __init__(self):
        self.lst = []

    def add(self, x):
        try:
            self.lst.append((x, min(x, self.lst[-1][1])))
        except IndexError:
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
