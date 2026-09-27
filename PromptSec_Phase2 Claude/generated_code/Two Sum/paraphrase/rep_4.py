def search_pair(numbers, sum_target):
    visited = {}
    for i, num in enumerate(numbers):
        remainder = sum_target - num
        if remainder in visited:
            return [visited[remainder], i]
        visited[num] = i
