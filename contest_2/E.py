n = int(input())
lst = list(map(int, input().split()))
stack = []
_min = 1
out = []
result = []
i = 0
try:
    while i < n:
        added = 0
        while lst[i] != _min:
            stack.append(lst[i])
            added += 1
            i += 1
        stack.append(lst[i])
        added += 1
        result.append([1, added])
        last = lst[i]
        outed = 0
        while len(stack) > 1 and stack[-2] - stack[-1] == 1:
            _min = stack.pop()
            out.append(_min)
            outed += 1
        if (stack[-1] == _min + 1 and outed != 0) or (outed == 0 and stack[-1] == _min):
            out.append(stack.pop())
            outed += 1
        result.append([2, outed])
        _min = out[-1] + 1
        i += 1
    if out == sorted(lst):
        print(len(result))
        for i in result:
            print(*i)
    else:
        print(0)
except:
    print(0)
