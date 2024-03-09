# просто нужно реализовать кучу с поддержкой максимума, она уже реализована в
# различных библиотеках, но в задаче попросили реализовать с нуля
# про ее реализацию проще будет прочитать в инете
# да и в принципе код, реализующий её и решающий задачу тоже можно нагуглить я думаю


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.up(len(self.heap) - 1)

    def extract(self):
        self.heap[len(self.heap) - 1], self.heap[0] = self.heap[0], self.heap[len(self.heap) - 1]
        root = self.heap.pop()
        self.down(0)
        return root

    def up(self, ind):
        root_ind = (ind - 1) // 2
        if root_ind < 0:
            return
        if self.heap[ind] > self.heap[root_ind]:
            self.heap[ind], self.heap[root_ind] = self.heap[root_ind], self.heap[ind]
            self.up(root_ind)

    def down(self, ind):
        child_ind = ind * 2 + 1
        if child_ind >= len(self.heap):
            return
        if child_ind + 1 < len(self.heap) and self.heap[child_ind] < self.heap[child_ind + 1]:
            child_ind += 1
        if self.heap[child_ind] > self.heap[ind]:
            self.heap[child_ind], self.heap[ind] = self.heap[ind], self.heap[child_ind]
            self.down(child_ind)


n = int(input())
heap = MaxHeap()
for _ in range(n):
    query = input()
    if query == '1':
        print(heap.extract())
    else:
        heap.insert(int(query.split()[1]))
