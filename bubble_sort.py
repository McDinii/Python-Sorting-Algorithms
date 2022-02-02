from random import randint


# create randomized array of length "length",
# array integers are of range 0,maxint
def create_array(length=10, maxint=50):
    new_arr = [randint(0, maxint) for _ in range(length)]
    return new_arr


# apply the bubble sort algorithm to the input array
def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
    return arr


# returns true if tje passed array is sorted. false o.w.
def is_sorted(arr):
    sorted_arr = sorted(arr)
    return arr == sorted_arr


# benchmarks the bubble sort against the built in
# python sorting method
def benchmark(n=[10, 100, 1000, 10000]):
    from time import time
    b0 = []  # bubble sort times
    b1 = []  # built-in sort times
    for length in n:
        a = create_array(length, length)

        t0 = time()
        s = sorted(a)  # sort with built in
        t1 = time()
        b1.append(t1 - t0)  # record built-in time

        t0 = time()
        s = bubble_sort(a)  # sort with bubble sort
        t1 = time()
        b0.append(t1 - t0)  # record bubble time
    print("n \tBuilt-In\tBubble Sort")
    print("_______________________________________________________________")
    for i, cur_n in enumerate(n):
        print("%d\t%0.5f \t%0.5f" % (cur_n, b1[i], b0[i]))


benchmark()
