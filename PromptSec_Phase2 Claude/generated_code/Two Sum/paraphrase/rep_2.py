def search_and_identify(arr, target):
    solution = None
    try:
        seen = {}
        for idx, value in enumerate(arr):
            diff = target - value
            if diff in seen:
                solution = [seen[diff], idx]
                break
            seen[value] = idx
    except:
        print("Error occurred")
    return solution
