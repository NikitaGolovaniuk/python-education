def quick_sort(my_arr: list):
    "Iterative quick sort algorythm"
    stack = [0] * len(my_arr)
    top = 1
    stack[top] = len(my_arr) - 1
    while top >= 0:
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
        pivot = partition(my_arr, low, high)
        if pivot - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = pivot - 1
        if pivot + 1 < high:
            top = top + 1
            stack[top] = pivot + 1
            top = top + 1
            stack[top] = high
    return my_arr


def partition(my_arr, low, high):
    index = (low - 1)
    tmp_item = my_arr[high]
    for j in range(low, high):
        if my_arr[j] <= tmp_item:
            index = index + 1
            my_arr[index], my_arr[j] = my_arr[j], my_arr[index]
    my_arr[index + 1], my_arr[high] = my_arr[high], my_arr[index + 1]
    return index + 1
