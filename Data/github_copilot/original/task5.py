def merge_intervals(intervals):
	if not intervals:
		return []
	ordered = sorted(intervals, key=lambda interval: interval[0])
	merged = [ordered[0][:]]
	for start, end in ordered[1:]:
		if start <= merged[-1][1]:
			merged[-1][1] = max(merged[-1][1], end)
		else:
			merged.append([start, end])
	return merged
