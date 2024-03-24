def build_suffix_array(s):
    s += "$"
    n = len(s)
    ranks = [ord(c) for c in s]
    sa = list(range(n))

    def sort_on_kth_character(ind):
        pairs = [(ranks[j], ranks[j + ind] if j + ind < n else -1, j) for j in range(n)]
        pairs.sort()
        return [j for _, _, j in pairs]

    k = 1
    while k < n:
        sa = sort_on_kth_character(0)
        tmp_ranks = [0] * n
        rank = 0
        for i in range(1, n):
            prev, curr = sa[i - 1], sa[i]
            if ranks[prev] != ranks[curr] or ranks[prev + k] != ranks[curr + k]:
                rank += 1
            tmp_ranks[curr] = rank
        ranks = tmp_ranks
        if ranks[sa[-1]] == n - 1:
            break
        k *= 2
    return sa


def find_with_one_mismatch(sa):
    positions = []
    len_p = len(p)
    n = len(t)

    def match_with_mismatch(ind):
        mismatch_count = 0
        for j in range(len(p)):
            if ind + j >= len(t) or t[ind + j] != p[j]:
                mismatch_count += 1
                if mismatch_count > 1:
                    return False
        if mismatch_count <= 1:
            return True
        else:
            return False

    for idx, i in enumerate(sa):
        if i + len_p <= n and match_with_mismatch(i):
            positions.append(i + 1)
    return positions


p = input()
t = input()
suffix_array = build_suffix_array(t)
result = find_with_one_mismatch(suffix_array)
print(len(result))
print(*sorted(result))
