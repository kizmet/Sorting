# TO-DO: Complete the selection_sort() function below
import random


def insertion_sort(arr):
    arr2 = []
    # loop through n-1 elements
    # for i in range(0, len(arr) - 1):
    while len(arr) > 0:
        cur_index = 0
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for n in range(1, len(arr)):
            if arr[n] < arr[smallest_index]:
                smallest_index = n
        arr2.append(arr.pop(smallest_index))
    # TO-DO: swap
    arr = arr2
    return arr


arr = random.sample(range(200), 50)

# y = sorted(arr)
# x = insertion_sort(arr)
# print(x )


def selection_sort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i
        while j > 0 and tmp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = tmp
    return arr


# arr = random.sample(range(200), 50)
# print(selection_sort(arr))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    arrlen = len(arr) - 1
    for i in range(0, arrlen):
        count = 0
        while count < arrlen:
            x = arr[count]
            y = arr[count + 1]
            if x > y:
                arr[count] = y
                arr[count + 1] = x
            count += 1
    return arr


arr = [3, 9, 1, 5, 6, 4]
x = bubble_sort(arr)
print(x)


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
