n, k = map(int, input().split())
lst = list(map(int, input().split()))
to_find = list(map(int, input().split()))
# перебираем число, максимально близкое к которому нужно найти в массиве
for x in to_find:
    # обозначаем левую и правую границы поиска по массиву в виде крайних индексов
    left = 0
    right = n - 1
    while right - left > 1:
        # вычисляем среднее значение по которому пляшет бинпоиск
        mid = (left + right) // 2
        # если в отсортированном массиве попали в число меньше искомого, значит сдвигаем левую границу правее
        if lst[mid] < x:
            left = mid
        # иначе сдвигаем правую границу левее
        else:
            right = mid
    # печатаем число из массива по тому индексу, элемент которого максимально близок к заданному числу
    if abs(lst[left] - x) <= abs(lst[right] - x):
        print(lst[left])
    else:
        print(lst[right])
