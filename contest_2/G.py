from collections import deque


def divide():
    while len(deque_2) > len(deque_1):
        deque_1.append(deque_2.popleft())


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
