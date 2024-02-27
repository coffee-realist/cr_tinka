from collections import deque

n = int(input())
d = deque()
for i in range(n):
    query = input()
    _type = int(query[0])
    if _type == 1:
        _id = int(query.split()[1])
        d.append(_id)
    elif _type == 2:
        d.popleft()
    elif _type == 3:
        d.pop()
    elif _type == 4:
        _id = int(query.split()[1])
        print(d.index(_id))
    elif _type == 5:
        print(d[0])
'''
7
1 1
5
1 3
3
2
1 2
4 2

'''