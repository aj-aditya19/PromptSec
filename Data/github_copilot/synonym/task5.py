def combine_ranges(ranges):
	if not ranges:
		return []
	ordered = sorted(ranges, key=lambda value: value[0])
	combined = [ordered[0][:]]
	for start, end in ordered[1:]:
		if start <= combined[-1][1]:
			combined[-1][1] = max(combined[-1][1], end)
		else:
			combined.append([start, end])
	return combined
