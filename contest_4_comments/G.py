# не заходит на питоне по времени, на плюсах еле заходит только с быстрым вводом/выводом и ещё одной ускорялкой
res = 0
n = int(input())
# кол-во секунд в дне
seconds_per_day = 60 * 60 * 24
# массив, в котором индекс - какая-то из секунд дня, а элемент по этому индексу - кол-во открытых касс в этот момент
seconds = [0 for i in range(seconds_per_day)]
for _ in range(n):
    # ввод времен и перевод в секунды
    opened_h, opened_m, opened_s, closed_h, closed_m, closed_s = map(int, input().split())
    opened = (opened_h * 60 + opened_m) * 60 + opened_s
    closed = (closed_h * 60 + closed_m) * 60 + closed_s
    # если время открытия и закрытия происходит в один и тот же день
    if opened < closed:
        for i in range(opened, closed):
            seconds[i] += 1
    # противный случай (например касса открылась в 8 утра, а закрылась в 2 ночи)
    else:
        for i in range(opened, seconds_per_day):
            seconds[i] += 1
        for i in range(closed):
            seconds[i] += 1
# выводим количество секунд, в которые работали все n касс
print(seconds.count(n))
