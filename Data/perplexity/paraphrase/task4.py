def efficient_search(sorted_list, value):
    """
    Implement a function in Python that, given a sorted list and a value to find, 
    efficiently narrows down the search range to locate the value's index, 
    or returns -1 if it isn't present.
    """
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == value:
            return mid
        elif sorted_list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return -1
