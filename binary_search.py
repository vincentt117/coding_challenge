def binarySearch(sortedList, targetVal):
	if not sortedList:
		return False
	else:
		start = 0
		end = len(sortedList) - 1
		while start < end:
			if sortedList[(end-start)//2 + start] == targetVal:
				return True
			elif sortedList[(end-start)//2 + start] > targetVal
				end = (end-start)//2 + start
			else:
				start = (end-start)//2 + start 
		return False

# Not fully tested