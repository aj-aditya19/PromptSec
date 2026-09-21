def find_index_binary(data, value_to_find):
    start, end = 0, len(data) - 1
    while start <= end:
        mid_point = (start + end) // 2
        if data[mid_point] == value_to_find:
            return mid_point
        if data[mid_point] < value_to_find:
            start = mid_point + 1
        else:
            end = mid_point - 1
    return -1
