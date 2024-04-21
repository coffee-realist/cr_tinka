from collections import deque
from math import inf


def min_digit_sum_divisible_by_k(k):
    if k == 1:
        return 1
    dp = [inf] * k
    d = deque()
    # определение цифр, которые можем использовать (все цифры меньше k)
    for i in range(1, 10):
        dp[i % k] = min(dp[i % k], i)
        d.append(i % k)
    while d:
        p = d.popleft()  # Извлекаем текущую последовательность найденных цифр из очереди
        for digit in range(10):  # Перебираем все возможные цифры
            new_p = (p * 10 + digit) % k  # Вычисляем новое значение остатка от деления
            new_sum = dp[p] + digit  # Вычисляем новую сумму цифр
            if new_sum < dp[new_p]:  # Если новая сумма меньше текущего значения в dp для этого остатка
                dp[new_p] = new_sum  # Обновляем значение в dp
                d.append(new_p)  # Добавляем новый остаток в очередь d
    if dp[0] != inf:
        return dp[0]
    else:
        return k


# Запускаем функцию с вводом k и выводим результат
print(min_digit_sum_divisible_by_k(int(input())))
