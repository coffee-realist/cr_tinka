from collections import deque

n = int(input())
d = deque()
database = [0] * 2 * 10 ** 5
out = 0
for i in range(n):
    query = input()
    _type = int(query[0])
    if _type == 1:
        _id = int(query.split()[1])
        database[_id] = len(d) + out
        d.append(_id)
    elif _type == 2:
        d.popleft()
        out += 1
    elif _type == 3:
        d.pop()
    elif _type == 4:
        _id = int(query.split()[1])
        print(database[_id] - out)
    elif _type == 5:
        print(d[0])
