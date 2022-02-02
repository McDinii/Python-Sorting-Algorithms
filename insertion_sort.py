from bubble_sort import bubble_sort
from selection_sort import selection_sort, create_array


# performs the selection sort algorithm on the passed
# list, returns the sorted version
def insertion_sort(a):
    for sort_len in range(1, len(a)):
        cut_item = a[sort_len]  # next unsorted item
        insert_idx = sort_len  # current index of item

        # iterate until we reach correct insert spot
        while insert_idx > 0 and cut_item < a[insert_idx - 1]:
            a[insert_idx] = a[insert_idx - 1]  # shift
            insert_idx -= 1  # decrement insert spot
        # insert item at the correct spot
        a[insert_idx] = cut_item
    return a


# benchmarks the built in against other sorts
# python sorting method
def benchmark(n=[10, 100, 1000, 10000]):
    from time import time
    b0 = []  # bubble sort times
    b1 = []  # built-in sort times
    b2 = []  # selection sort times
    b3 = []  # insertion sort times
    for size in n:
        a = create_array(size, size)

        t0 = time()
        s = sorted(a)  # sort with built in
        t1 = time()
        b1.append(t1 - t0)  # record built-in time

        t0 = time()
        s = bubble_sort(a)  # sort with bubble sort
        t1 = time()
        b0.append(t1 - t0)  # record bubble time

        t0 = time()
        s = selection_sort(a)  # sort with selection sort
        t1 = time()
        b2.append(t1 - t0)  # record selection time

        t0 = time()
        s = insertion_sort(a)  # sort with insertion sort
        t1 = time()
        b3.append(t1 - t0)  # record insertion time
    print("n   \tBuilt-In|\tBubble Sort|\tSelection Sort|\tInsertion Sort|")
    print("_______________________________________________________________")
    for i, cur_n in enumerate(n):
        print("%5d\t%0.6f|\t%0.9f|\t%0.12f|\t%0.12f" % (cur_n, b1[i], b2[i], b0[i], b3[i]))


benchmark()
a = create_array()
print("Unsorted:", a)
a = insertion_sort(a)
print("Sorted  :", a)