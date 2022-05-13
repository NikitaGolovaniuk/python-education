def binary_search(input_arr: list, value: int):
    """return first element index with value"""
    l_pointer = 0
    r_pointer = len(input_arr)-1
    while l_pointer <= r_pointer:
        mid = (l_pointer + r_pointer) // 2
        if input_arr[mid] == value:
            return mid
        elif input_arr[mid] < value:
            l_pointer = mid + 1
        else:
            r_pointer = mid - 1