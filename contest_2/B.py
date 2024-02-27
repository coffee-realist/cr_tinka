class DoubleStack:
    def __init__(self):
        self.left = []
        self.right = []
        self.right_min = 1e9

    def add_right(self, x):
        self.right.append(x)
        self.right_min = min(x, self.right_min)

    def pop_first(self):
        if len(self.left) == 0:
            _min = 1e9
            while len(self.right):
                _min = min(_min, self.right.pop())
                self.left.append(_min)
            self.right_min = 1e9
        self.left.pop()

    def min(self):
        if len(self.left):
            return min(self.right_min, self.left[-1])
        return self.right_min


n, k = map(int, input().split())
lst = list(map(int, input().split()))
double_stack = DoubleStack()
for i in lst[:k]:
    double_stack.add_right(i)
for i in range(k, n):
    print(double_stack.min(), end=' ')
    double_stack.add_right(lst[i])
    double_stack.pop_first()
print(double_stack.min(), end=' ')
