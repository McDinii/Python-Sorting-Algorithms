from bubble_sort import bubble_sort


# crates array if length "size" , each element is
# randomly selected from the range (0,max)
def create_array(size=10, maxint=50):
    from random import randint
    return [randint(0, maxint) for _ in range(size)]


# performs the selection sort algorithm on the passed
# list, returns the sorted version
def selection_sort(a):
    sort_len = 0  # length of current sorted portion
    while sort_len < len(a):
        min_idx = None  # index of smallest item found
        for i, elem in enumerate(a[sort_len:]):
            # check current elem to see if smallest
            if min_idx is None or elem < a[min_idx]:
                # update with current smallest
                min_idx = i + sort_len
        a[sort_len], a[min_idx] = a[min_idx], a[sort_len]
        sort_len += 1
    return a


# benchmarks the built in against other sorts
# python sorting method
def benchmark(n=[10, 100, 1000, 10000]):
    from time import time
    b2 = []  # selection sort times
    b1 = []  # built-in sort times
    b0 = []  # bubble sort times
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
    print("n   \tBuilt-In|\tBubble Sort|\tSelection Sort|")
    print("_______________________________________________________________")
    for i, cur_n in enumerate(n):
        print("%5d\t%0.6f|\t%0.9f|\t%0.12f|" % (cur_n, b1[i], b2[i], b0[i]))


# benchmark()
# a = create_array()
# print("Unsorted:", a)
# a = selection_sort(a)
# print("Sorted  :", a)
