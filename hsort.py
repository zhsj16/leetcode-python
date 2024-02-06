import random

a = [random.randint(0, 99) for _ in range(10)]
n = len(a)


def adjust(start, end):
    root = start
    child = 2 * root + 1
    while child <= end:
        if child + 1 <= end and a[child + 1] > a[child]:
            child += 1
        if a[root] < a[child]:
            a[root], a[child] = a[child], a[root]
            root = child
            child = 2 * child + 1
        else:
            break


def hsort():
    mid = n // 2 - 1
    for start in range(mid, -1, -1):
        adjust(start, n - 1)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        adjust(0, end - 1)


print(a)
hsort()
print(a)
