from math import inf


# немножко множко укуренно-костыльный какой-то бинпоиск, по-любому можно было сделать проще и лучше, но я не смог (
def bin_search(left, right, _type):
    # бесконечно большое число
    min_delta = inf
    # здесь будем хранить последний мид, чтобы в случае чего не зациклиться
    # (в адекватном бинпоиске такой хрени быть не должно, но я тут уже всю надежду успел трижды потерять, так что да)
    last_mid = -1
    # тут будем хранить лучшие ответы, мне это понадобилось, чтобы совладать с условием последнего абзаца вых. данных
    answers = []
    while True:
        mid = (left + right + 1) // 2
        s_1, s_2 = f(_type, mid - 1)
        delta = s_2 - s_1
        # ищем минимальное отклонение и по нему храним все ответы в answers
        if abs(delta) < abs(min_delta):
            min_delta = delta
            min_mid = mid
            answers = [min_mid]
        elif abs(delta) == abs(min_delta):
            answers.append(mid)
        # если отклонение между суммами больше нуля, то значит сумма во втором прямоугольнике чисел больше,
        # а нам при этом не нужно чтобы она стала ещё больше, поэтому сдвигаем левую границу, иначе, аналогично, правую
        if delta >= 0:
            left = mid
        else:
            right = mid
        # условие выхода из вайла, когда начал циклиться mid
        if mid == last_mid:
            break
        last_mid = mid
    return _type, min(answers), min_delta


# выглядит страшно, но это тупо матан, можно считать сумму чисел в прямоугольниках и циклами,
# но по-моему тогда решение не зайдет по времени
def f(t, x):
    if t == 'V':
        # сумма арифметической прогрессии сумм арифметических прогрессий
        s_1 = ((1 + x) * x // 2 + ((m * (n - 1) + 1) + (m * (n - 1) + x)) * x // 2) * n // 2
    else:
        # сумма арифметической прогрессии
        s_1 = (1 + m * x) * m * x // 2
    # сумма чисел во втором прямоугольнике как общая сумма минус сумма чисел в первом
    s_2 = (1 + n * m) * n * m // 2 - s_1
    return s_1, s_2


for _ in range(int(input())):
    n, m = map(int, input().split())
    # делаем два бинпоиска, по вертикальному и по горизонтальному разрезам
    s_v, k_v, d_v = bin_search(1, m, 'V')
    s_h, k_h, d_h = bin_search(1, n, 'H')
    # смотрим какой выдал ответ с наименьшим отклонением
    if abs(d_v) <= abs(d_h):
        print(s_v, k_v)
    else:
        print(s_h, k_h)
