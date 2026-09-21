def merge_intervals(intervals):
	if not intervals:
		return []
	intervals = sorted(intervals, key=lambda pair: pair[0])
	result = [intervals[0][:]]
	for current in intervals[1:]:
		if current[0] <= result[-1][1]:
			result[-1][1] = max(result[-1][1], current[1])
		else:
			result.append(current[:])
	return result
