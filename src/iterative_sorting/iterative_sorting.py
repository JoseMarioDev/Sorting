# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # loop through array starting with index[1], compare values
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                print(f"compare {arr[j]} and {arr[smallest_index]}")
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        print(f"Swapped {arr[i]} with {arr[smallest_index]}")

    return arr


# my own test to see what's going on
# time complexity is O(n^2) because of nested loop?

my_array = [5, 4, 3, 2, 1]
print(selection_sort(my_array))


# TO-DO:  implement the Bubble Sort function below

def bubble_sort(arr):
    for k in range(len(arr)):
        for l in range(len(arr) - k - 1):
            if arr[l] > arr[l + 1]:
                arr[l], arr[l + 1] = arr[l + 1], arr[l]

    return arr


my_array = [6, 4, 3, 2, 1]
print(bubble_sort(my_array))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
