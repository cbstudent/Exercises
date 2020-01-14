def longestPalindromicSubstring(string):
    longest = [0, 1]
	for i in range(1, len(string)):
		even = checkIsLongest(string, i-1, i+1)
		odd = checkIsLongest(string, i-1, i)
		curLongest = max(even, odd, key = lambda x: x[1] - x[0])
		longest = max(curLongest, longest, key = lambda x: x[1] - x[0])
	return string[longest[0]:longest[1]]

def checkIsLongest(string, leftIdx, rightIdx):
	while leftIdx >= 0 and rightIdx < len(string):
		if string[leftIdx] != string[rightIdx]:
			break
		leftIdx -= 1
		rightIdx += 1
	return  [leftIdx + 1, rightIdx]
