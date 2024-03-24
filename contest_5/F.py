def count(lst, t):
    left = 0 - t
    right = 0 - t
    p = (t + 1) % 2
    for i in range(p, n - t):
        if i < right:
            lst[i] = min(lst[left + right - i - t], right - i + p)
        while i - lst[i] >= 0 and i + lst[i] + t < n and s[i - lst[i]] == s[i + lst[i] + t]:
            lst[i] += 1
        if i + lst[i] - p > right:
            left = i - lst[i] + 1
            right = i + lst[i] - p
    return lst


s = input()
n = len(s)
print(sum(count([1] * n, 0)) + sum(count([0] * (n - 1), 1)))
