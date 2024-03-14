def get_cows_cnt(x):
    last = lst[0]
    cnt = 1
    # перебираем координаты стойл
    for i in lst[1:]:
        # смотрим если расстояние между стойлами больше ответа, то всё отлично (т.к. ответ это минимум)
        # тогда обновляем последний элемент и инкриминируем счетчик коров
        if i - last >= x:
            last = i
            cnt += 1
    return cnt


n, k = map(int, input().split())
lst = list(map(int, input().split()))
# самый стандартный бинпоиск по ответу
left = 1
right = lst[-1]
while right - left > 1:
    mid = (left + right) // 2
    # перебираем разный ответ на задачу и относительно него функцией вычисляем количество коров
    # потом проверяем подходит ли это кол-во коров под заданное k
    if get_cows_cnt(mid) < k:
        right = mid
    else:
        left = mid
print(left)
