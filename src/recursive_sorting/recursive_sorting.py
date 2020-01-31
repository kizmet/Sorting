# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    m = 0
    while a < len(arrA) and b < len(arrB):
        # print("a", a, "b", b)
        # print(arrA[a])
        if arrA[a] < arrB[b]:
            merged_arr[m] = arrA[a]
            a += 1
        else:
            merged_arr[m] = arrB[b]
            b += 1
        m += 1

    while a < len(arrA):
        merged_arr[m] = arrA[a]
        a += 1
        m += 1

    while b < len(arrB):
        merged_arr[m] = arrB[b]
        b += 1
        m += 1

    return merged_arr


y = merge([0, 3, 4, 5, 8], [1, 2, 6, 7, 9])
print(y)
# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[mid:]
        right = arr[:mid]
        arr = merge(merge_sort(left), merge_sort(right))
        return arr


arr = [5, 1, 8, 4, 2, 9, 6, 0, 3, 7]
x = merge_sort(arr)
print(x)


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        arrA = [i for i in arr[1:] if i <= pivot]
        arrB = [i for i in arr[1:] if i > pivot]
        return merge_sort(arrA) + [pivot] + merge_sort(arrB)


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
