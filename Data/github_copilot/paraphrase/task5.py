def merge_overlapping_pairs(pairs):
	if not pairs:
		return []
	ordered = sorted(pairs, key=lambda pair: pair[0])
	result = [ordered[0][:]]
	for start, end in ordered[1:]:
		if start <= result[-1][1]:
			result[-1][1] = max(result[-1][1], end)
		else:
			result.append([start, end])
	return result
