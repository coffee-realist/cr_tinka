def merge_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        mid = int(len(lst) / 2)
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)


def merge(left, right):
    global cnt
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
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged


cnt = 0
int(input())
result = merge_sort(list(map(int, input().split())))
print(cnt)
print(*result)
