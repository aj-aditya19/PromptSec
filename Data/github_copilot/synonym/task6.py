def longest_unique_length(text):
	last_seen = {}
	beginning = longest = 0
	for index, character in enumerate(text):
		if character in last_seen:
			beginning = max(beginning, last_seen[character] + 1)
		last_seen[character] = index
		longest = max(longest, index - beginning + 1)
	return longest
