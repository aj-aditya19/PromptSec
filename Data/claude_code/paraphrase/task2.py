def two_sum(numbers, target_sum):
    lookup = {}
    for index in range(len(numbers)):
        remainder = target_sum - numbers[index]
        if remainder in lookup:
            return [lookup[remainder], index]
        lookup[numbers[index]] = index
    return []
