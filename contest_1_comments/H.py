# ! проверяющая система тварь, нужно указывать перед отправкой пустой предпочитаемый конец строк !
n = int(input())
s = input()
frequency = dict()
result = ''
# подсчитываем в словаре частоту каждой из букв
for letter in s:
    try:
        frequency[letter] += 1
    except KeyError:
        frequency[letter] = 1
# буквы, которых четно кол-во нужно вывести все; нечетные - их кол-во минус 1,
# потому что не обязательно использовать все буквы, потом из нечетных нужно выбрать самую большую по частоте и
# воткнуть в центр

# бежим по отсортированным ключам, то бишь буквам и печатаем их в 2 раза меньше, чем они есть, формируя 1-ую половину
for letter in sorted(frequency.keys()):
    result += letter * (frequency[letter] // 2)
# ищем нечетную букву для серединки (самую крутышку)
mid = ''
for letter in sorted(frequency.keys()):
    if frequency[letter] % 2:
        mid = letter
        break
# печатаем первую половину, найденную серединку и перевернутую первую половину (палиндром как никак)
print(result + mid + result[::-1])
