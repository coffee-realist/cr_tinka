n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
# сортируем отрезки по их началам, чтобы идти по порядку
# сортируем в обратном порядке, чтобы удобно и быстро можно было обрабатывать отрезки,
# работая с концом стека (массива), а не с его началом
lst.sort(reverse=True)
# первый отрезок точно берем и добавляем длину в ответ
left, right = lst.pop()
result = right - left
while len(lst):
    if len(lst):
        # извлекаем отрезки до тех пор, пока стек не опустеет или не найдем отрезок,
        # конец которого лежит за пределами последнего, взятого в ответ
        current = lst.pop()
        while len(lst) and current[-1] <= right:
            current = lst.pop()
        # если всё-таки нашли такой отрезок
        if current[-1] > right:
            # и его начало лежит до конца последнего взятого
            if current[0] < right:
                # то последний отрезок теперь начинается в своем конце, а заканчивается в конце найденного отрезка
                left = right
                right = current[-1]
            else:
                # иначе новый последний отрезок - это найденный отрезок
                left, right = current
            # обновляем результат
            result += right - left
print(result)