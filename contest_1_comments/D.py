c = float(input())
# смотрим по уравнению в каких границах может математически лежать ответ
left = -1
right = 10 ** 10  # тупо большая чиселка
# точность бинпоиска
eps = 0.0000001
while right - left > eps:
    # функция возрастает, значит ее значения отсортированы
    # здесь уже делаем бинпоиск по ответу, считая функцию и проверяя попадет она меньше c либо больше
    x = (left + right) / 2
    f = x * x + (x + 1) ** (1 / 2)
    if f < c:
        left = x
    else:
        right = x
print(right)