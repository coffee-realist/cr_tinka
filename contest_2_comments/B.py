# нужна структура, умеющая добавлять в конец и удалять из начала за O(1) - это по сути очередь
# можно использовать встроенную queue, либо создать свою структуру, как я и сделал, она состоит из двух стеков
# также нужно хранить минимум очереди, который можно будет получать так же за O(1)
class DoubleStack:
    def __init__(self):
        # очередь реализована через 2 стека, с одного удаляем элементы, в другой добавляем
        # при чем нам не особо важно какие элементы мы будем удалять, важно только какие будем добавлять
        # поэтому в левом стеке будем хранить только минимумы, элементы массива там ни к чему
        # значит минимум в левом стеке, будет лежать всегда сверху
        # а для правого будем хранить его в отдельной переменной
        self.left = []
        self.right = []
        self.right_min = 1e9

    def add_right(self, x):
        # добавляем в правый и обновляем минимум
        self.right.append(x)
        self.right_min = min(x, self.right_min)

    def pop_first(self):
        # если в левом закончились элементы, перекинем все элементы из правого в левый
        # но в левом не обязательно хранить элементы, поэтому будем добавлять в него минимум
        if len(self.left) == 0:
            _min = 1e9
            while len(self.right):
                _min = min(_min, self.right.pop())
                self.left.append(_min)
            # правый опустел, обновляем минимум
            self.right_min = 1e9
        self.left.pop()

    def min(self):
        # минимальный элемент всегда будет лежать либо на верху левого стека, либо в переменной минимума правого
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
