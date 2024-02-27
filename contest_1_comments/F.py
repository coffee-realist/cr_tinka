# функция сортировки слиянием
def merge_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        mid = int(len(lst) / 2)
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)


# вспомогательная для сортировки функция слияния двух отсортированных массивов в один
def merge(left, right):
    global cnt  # чтобы можно было менять глобальную переменную внутри функции
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            cnt += len(left) - i
            # число инверсий на момент сравнения двух элементов это количество элементов из левого массива,
            # находящихся справа от текущего левого элемента, который оказался больше, чем текущий правый
            # почему? потому что массивы на входе отсортированы.
            # пример: left = [4, 5, 6]; right = [1, 2, 3]; left[i] = 4; right[j] = 1; left[i] > right[j] =>
            # => left[i + 1], left[i + 2], ..., left[n - 1] > right[j] => current_cnt = len(left) - i
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged


# (функции сортировки я просто взял из инета и чутка подредачил под себя,)
# (ну а потом добавил в них 2 строчки для подсчёта числа инверсий)

# глобальный счётчик инверсий
cnt = 0
int(input())  # да
result = merge_sort(list(map(int, input().split())))
print(cnt)
print(*result)
