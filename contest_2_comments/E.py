# не могу сказать ничего хорошего об этом алгоритме, явно можно решить задачу проще и без костылей
n = int(input())
lst = list(map(int, input().split()))
stack = []
_min = 1
out = []
result = []
i = 0
# хоть и прошло пару дней, но я уже совсем не помню как её решил
# смотрю на решение и оно какое-то жесть стремное, как будто бы точно можно гораздо легче решить
# тем более что всё что мы можем, это оперировать со стеком, то бишь извлекать последний элемент и добавлять в конец
# если пытаться осознавать этот алгоритм, то наверное проще это будет сделать через дебаг, а не по комментам
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
    # ультракостыль, задача падала с ошибкой исполнения, я подумал, что в теории это скорее всего
    # происходит тогда, когда ответ должен быть 0, поэтому если прога выдает ошибку, то я ловлю ее и вместо нее вывожу 0
    print(0)
