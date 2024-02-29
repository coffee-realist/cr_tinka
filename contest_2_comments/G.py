from collections import deque


def divide():
    while len(deque_2) > len(deque_1):
        deque_1.append(deque_2.popleft())


# опять нужны все операции за O(1)
# а добавлять в середину за O(1) нельзя
# поэтому разобьем очередь пополам
# добавлять будем только во вторую (в ее начало, если элита, и в конец в противном случае)
# ну и нужно следить, чтобы длина второй очереди не превышала длину первой, а
# как только это происходит, то перекидывать гоблинов из начала второй в конец первой (функция divide)
deque_1 = deque()
deque_2 = deque()
for _ in range(int(input())):
    query = input()
    if query[0] == '+':
        _id = int(query.split()[1])
        deque_2.append(_id)
    elif query[0] == '*':
        _id = int(query.split()[1])
        deque_2.appendleft(_id)
    else:
        print(deque_1.popleft())
    divide()
