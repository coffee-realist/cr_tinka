n = int(input())
lst = list(map(int, input().split()))
m = int(input())
# просто считаем префиксные суммы
# (текущий элемент префиксных сумм равен сумме предыдущей суммы с текущим элементом массива)
prefix_sums = [0]
for i in lst:
    prefix_sums.append(prefix_sums[-1] + i)
# аналогичным образом считаем префиксные xor'ы
prefix_xors = [0]
for i in lst:
    prefix_xors.append(prefix_xors[-1] ^ i)
for _ in range(m):
    operation, left, right = map(int, input().split())
    # считаем и выводим нужную нам операцию на отрезке [left; right]
    if operation == 1:
        print(prefix_sums[right] - prefix_sums[left - 1])
    else:
        print(prefix_xors[right] ^ prefix_xors[left - 1])
