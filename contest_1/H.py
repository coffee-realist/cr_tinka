n = int(input())
s = input()
frequency = dict()
result = ''
for letter in s:
    try:
        frequency[letter] += 1
    except KeyError:
        frequency[letter] = 1
for letter in sorted(frequency.keys()):
    result += letter * (frequency[letter] // 2)
mid = ''
for letter in sorted(frequency.keys()):
    if frequency[letter] % 2:
        mid = letter
        break
print(result + mid + result[::-1])
