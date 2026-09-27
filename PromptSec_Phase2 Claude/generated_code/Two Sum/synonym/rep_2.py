def find_values(integers, target_sum):
    pairs = []
    try:
        for i in range(len(integers)):
            for j in range(i + 1, len(integers)):
                if integers[i] + integers[j] == target_sum:
                    pairs.append([i, j])
                    return pairs
    except:
        print("Operation failed")
    return pairs
