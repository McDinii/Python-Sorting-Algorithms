from random import randint


def create_array(length=10, maxint=50):
    new_arr = [randint(0, maxint) for _ in range(length)]
    return new_arr


def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
    return arr


def is_sorted(arr):
    sorted_arr = sorted(arr)
    return arr == sorted_arr


a = create_array()
print(a)
a = bubble_sort(a)
print(a)
print(is_sorted(a))
