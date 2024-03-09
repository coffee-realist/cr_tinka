import sys

# в питоне максимальная глубина рекурсии 1000,
# для большинства задач этого не хватает и код падает с ошибкой исполнения;
# поэтому мы вот этой функцией увеличиваем этот параметр
sys.setrecursionlimit(1000000)
# p.s. pypy хоть и ускоряет код на питоне, но делает это посредством жертвования
# некоторыми его функциями насколько я понимаю, поэтому если отправляешь код на pypy,
# а он падает с ошибкой исполнения или превышением реального времени работы,
# то стоит залить его на python;
# конкретно в случае этой задачи pypy не поддерживает значительного изменения
# пределов глубины рекурсии, которое мы делаем и падает с ошибкой исполнения,
# поэтому нужно заливать на питоне, как и большинство задач этого контеста


# если честно, то объяснять решения деревьев текстом для меня очень тяжело,
# поэтому мало что буду писать в комментах, могу постараться объяснить устно
def find_diameter(root):
    result = 1

    def dfs(k):
        nonlocal result
        children = [0, 0]
        lst = [dfs(child) for child in tree[k][1]]
        if len(lst):
            children = lst
        result = max(result, sum(sorted(children)[-2:]) + 1)
        return max(children) + 1

    dfs(root)
    return result - 1


n = int(input())
parents = list(map(int, input().split()))
tree = {0: [0, []]}
for i in range(len(parents)):
    tree[parents[i]][-1].append(i + 1)
    tree[i + 1] = [tree[parents[i]][0] + 1, []]
ans = []
for v in sorted(tree.keys()):
    ans.append(tree[v][0])
print(max(ans), find_diameter(0))
print(*ans)
