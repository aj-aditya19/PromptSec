def two_sum(numbers, goal):
    m = {}
    for index in range(len(numbers)):
        remainder = goal - numbers[index]
        if remainder in m:
            return [m[remainder], index]
        m[numbers[index]] = index
