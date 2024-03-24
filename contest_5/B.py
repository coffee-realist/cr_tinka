def z_function(string):
    string_len = len(string)
    z = [0] * string_len
    left = 0
    right = 0
    for i in range(1, string_len):
        z[i] = max(0, min(right - i, z[i - left]))
        while i + z[i] < string_len and string[z[i]] == string[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left = i
            right = i + z[i]
    return z


s = input()
n = len(s)
m = int(input())
for _ in range(m):
    cur = input()
    cur_len = len(cur)
    z_func = z_function(f'{cur}#{s}')
    result = []
    for j in range(cur_len + 1, len(z_func)):
        if z_func[j] == cur_len:
            result.append(j - cur_len - 1)
    print(len(result), *result)
