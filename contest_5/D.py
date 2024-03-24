s = input()
n = len(s)
split_index = 0
fail_func = [-1 for _ in range(n * 2)]
cur_split = 1
while cur_split < n * 2:
    cur = fail_func[cur_split - split_index - 1]
    while cur != -1 and s[cur_split % n] != s[(split_index + cur + 1) % n]:
        if s[cur_split % n] < s[(split_index + cur + 1) % n]:
            split_index = cur_split - cur - 1
        cur = fail_func[cur]
    if cur == -1 and s[cur_split % n] != s[split_index % n]:
        if s[cur_split % n] < s[(split_index + cur + 1) % n]:
            split_index = cur_split
        fail_func[cur_split - split_index] = cur
    else:
        fail_func[cur_split - split_index] = cur + 1
    cur_split += 1
print(s[split_index:] + s[:split_index])
