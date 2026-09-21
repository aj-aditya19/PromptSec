def longest_distinct_stretch(text):
	last_seen = {}
	start = result = 0
	for index, character in enumerate(text):
		if character in last_seen:
			start = max(start, last_seen[character] + 1)
		last_seen[character] = index
		result = max(result, index - start + 1)
	return result
