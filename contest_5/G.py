def find_longest_subanagram():
    max_length = 0
    min_len = min(len(lst_1), len(lst_2))
    hash_table_1 = {}
    hash_table_2 = {}
    for length in range(1, min_len + 1):
        hash_table_1[length] = {}
        hash_table_2[length] = {}

        for i in range(len(lst_1) - length + 1):
            subseq_hash = hash(tuple(sorted(lst_1[i:i + length])))
            if subseq_hash in hash_table_1[length]:
                hash_table_1[length][subseq_hash].append(i)
            else:
                hash_table_1[length][subseq_hash] = [i]

        for i in range(len(lst_2) - length + 1):
            subseq_hash = hash(tuple(sorted(lst_2[i:i + length])))
            if subseq_hash in hash_table_2[length]:
                hash_table_2[length][subseq_hash].append(i)
            else:
                hash_table_2[length][subseq_hash] = [i]

    for length in range(1, min_len + 1):
        for hash_val in hash_table_1[length]:
            if hash_val in hash_table_2[length]:
                max_length = max(max_length, length)

    return max_length


n = int(input())
lst_1 = list(map(int, input().split()))
m = int(input())
lst_2 = list(map(int, input().split()))
result = find_longest_subanagram()
print(result)
