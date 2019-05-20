import timeit
import matplotlib.pyplot as plt

from benchmark_between_sort_methods import quick_sort_implements


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


if __name__ == '__main__':
    lengths = []
    times_0 = []
    times_mid3 = []

    t = timeit.Timer('sort(alist)', 'from __main__ import sort,alist')
    for length in range(10, 501, 10):
        lengths.append(length)
        # print(lengths)
        alist = list(range(length, 0, -1))

        sort = quickSort
        times_0.append(t.timeit(10))

        sort = quick_sort_implements.quickSort
        times_mid3.append(t.timeit(10))

plt.plot(lengths, times_0, 'o',label='initial')
plt.plot(lengths, times_mid3, 'o',label='mid3')
plt.legend()
plt.show()
