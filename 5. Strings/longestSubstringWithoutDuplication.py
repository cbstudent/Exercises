def longestSubstringWithoutDuplication(string):
    lastSeen = {}
	
	left = 0
	right = 0
	
	longest = [0, 1]
	
	for right in range(len(string)):
		
		if lastSeen.get(string[right]):
			left = max(left, lastSeen.get(string[right]) + 1)
		lastSeen[string[right]] = right
		
		if right - left + 1 > longest[1] - longest[0]:
			longest = [left, right + 1]
	
	return string[longest[0]:longest[1]]
	
