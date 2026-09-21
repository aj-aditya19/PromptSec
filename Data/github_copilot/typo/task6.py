def longest_substring_length(s):
	positions = {}
	start = longest = 0
	for index, character in enumerate(s):
		if character in positions:
			start = max(start, positions[character] + 1)
		positions[character] = index
		longest = max(longest, index - start + 1)
	return longest
