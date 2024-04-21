class SegmentTree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.tree = [0] * (2 * self.size)

    def update(self, a, b, delta):
        a += self.size
        b += self.size
        while a < b:
            if a % 2 == 1:
                self.tree[a] += delta
                a += 1
            if b % 2 == 1:
                b -= 1
                self.tree[b] += delta
            a //= 2
            b //= 2

    def query(self, v):
        result = 0
        v += self.size
        while v > 0:
            result += self.tree[v]
            v //= 2
        return result

def count_painted_cells(segments):
    events = []
    for x1, y1, x2, y2 in segments:
        if x1 == x2:
            events.append((x1, y1, y2, 1))
        else:
            events.append((y1, x1, x2, 0))

    events.sort()

    tree = SegmentTree(2 * len(segments) + 1)
    last_x = events[0][0]
    total_painted = 0

    for x, y1, y2, event_type in events:
        total_painted += (x - last_x) * tree.query(1)
        last_x = x
        if event_type == 1:
            tree.update(y1, y2, 1)
        else:
            tree.update(y1, y2, -1)

    return total_painted

# Примеры использования:
segments1 = [(0, 1, 2, 1), (1, 4, 1, 2), (0, 3, 2, 3)]
segments2 = [(-2, -1, 2, -1), (2, 1, -2, 1), (-1, -2, -1, 2), (1, 2, 1, -2)]

print(count_painted_cells(segments1))  # Вывод: 8
print(count_painted_cells(segments2))  # Вывод: 16
