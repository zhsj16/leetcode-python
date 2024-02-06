import random

a = [random.randint(0, 99) for _ in range(10)]


def qsort(l, r):
    if l > r:
        return
    i, j = l, r
    t = a[l]
    while i < j:
        while i < j and a[j] >= t:
            j -= 1
        while i < j and a[i] <= t:
            i += 1
        a[i], a[j] = a[j], a[i]
    a[l] = a[i]
    a[i] = t
    qsort(l, i - 1)
    qsort(i + 1, r)


print(a)
qsort(0, len(a) - 1)
print(a)
