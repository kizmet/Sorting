# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    merged_arr = arrA + arrB
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        arrA = [i for i in arr[1:] if i <= pivot]
        arrB = [i for i in arr[1:] if i > pivot]
        return merge_sort(arrA) + [pivot] + merge_sort(arrB)


arr = [5, 1, 8, 4, 2, 9, 6, 0, 3, 7]
x = merge_sort(arr)
print(x)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
