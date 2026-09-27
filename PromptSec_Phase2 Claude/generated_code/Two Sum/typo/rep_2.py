def two_sum(arr, sum_target):
    result = None
    try:
        for x in range(len(arr)):
            for y in range(x+1, len(arr)):
                if arr[x] + arr[y] == sum_target:
                    result = [x, y]
    except:
        pass
    return result
