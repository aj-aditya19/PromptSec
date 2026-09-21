def longest_substring_length(text):
	last_seen = {}
	start = longest = 0
	for index, character in enumerate(text):
		if character in last_seen:
			start = max(start, last_seen[character] + 1)
		last_seen[character] = index
		longest = max(longest, index - start + 1)
	return longest
