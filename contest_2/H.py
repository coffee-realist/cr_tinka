# не решена
def min_pair2():
    idx = [[-1, -1]]
    for i in range(1, n):
        j = i - 1
        if lst[j] < lst[i]:
            idx.append([j, i])
        else:
            for j in range(len(idx) - 1, -1, -1):
                if lst[idx[j][0]] < lst[i]:
                    idx.append([idx[j][0], i])
                    break
            else:
                idx.append([-1, -1])
    return idx


def choose_best_sum(min_ind, elem_ind):
    if elem_ind == -1:
        return -1
    sums = set()
    sums.add((prefix_sums[elem_ind] - prefix_sums[min_ind - 1]) * lst[min_ind])
    sums.add((prefix_sums[elem_ind] - prefix_sums[min_ind]) * lst[elem_ind])
    sums.add((prefix_sums[elem_ind - 1] - prefix_sums[min_ind]) * lst[mins[elem_ind - 1][0]])
    return max(sums)


n = int(input())
lst = list(map(int, input().split()))
mins = min_pair2()
print(mins)
prefix_sums = [0]
for i in lst:
    prefix_sums.append(prefix_sums[-1] + i)
prefix_sums.pop(0)
print(prefix_sums)
mx = -1e20
for l, r in mins:
    cur = choose_best_sum(l, r)
    if cur > mx:
        mx = cur
print(mx)
'''
6
3 1 6 4 5 2

'''
