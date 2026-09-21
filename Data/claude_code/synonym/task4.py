def binary_lookup(sorted_list, goal_value):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if sorted_list[middle] == goal_value:
            return middle
        elif sorted_list[middle] < goal_value:
            left = middle + 1
        else:
            right = middle - 1
    return -1
