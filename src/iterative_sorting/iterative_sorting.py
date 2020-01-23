# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        print(f"Swapped {arr[i]} with {arr[smallest_index]}")

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for k in range(len(arr)):
        for l in range(len(arr) - k - 1):
            if arr[l] > arr[l + 1]:
                arr[l], arr[l + 1] = arr[l + 1], arr[l]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
