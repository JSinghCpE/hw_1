import heapq

import math


class Point:
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y

    def dist2(self, a, b):
        dx = a - self.x
        dy = b - self.y
        return (-1) * (dx ** 2 + dy ** 2)


k = int(input("Enter value for k >> "))
m = int(input("Enter value for m >> "))
filename = input("Enter path to file >> ")

with open(filename) as f:
    a = 0
    b = 0
    while not (a == 1 and b == 1):
        coordinate = input("Enter coordinate to classify >> ").split()
        a = float(coordinate[0])
        b = float(coordinate[1])
        heap = []
        i = 0
        f.seek(0)
        while i < m:
            line = f.readline()
            if line == "":
                break
            line = line.split()
            p = Point(line[0], float(line[1]), float(line[2]))
            if (len(heap) < k):
                heapq.heappush(heap, (p.dist2(a, b), p))
            else:
                heapq.heappushpop(heap, (p.dist2(a, b), p))
        heap.sort(reverse=True)
        labels = []
        counts = []
        for p in heap:
            if p[1].label in labels:
                counts[labels.index()] += 1
            # else:
                # labels[p[1].label] =

            print(p[1].label, "{:5.2f}".format(p[1].x), "{:5.2f}".format(p[1].y),
                  "{:5.2f}".format(math.sqrt(-1 * p[0])))
