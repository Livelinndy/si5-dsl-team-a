import re

timePattern = re.compile("^((\d{1,2}h)?\d{1,2}m)?\d{1,2}s$")

def timeToSeconds(timeStr):
	if timePattern.match(timeStr):
		timeArr = re.split('h|m|s', timeStr)
		del timeArr[-1] # removing the last element which is ''
		res = 0
		m = 1
		l = len(timeArr) - 1
		for i in range(l, -1, -1):
				res = res + (int(timeArr[i]) * m)
				m = m * 60
		return res
	else:
		raise Exception("timeStr doesn't match the pattern")
'''
def timeBetween(startTime, endTime):
	start = timeToSeconds(startTime)
	end = timeToSeconds(endTime)
	if end < start:
		raise Exception("Cannot set end time before start time")
	return end - start
'''
def hexToRgb(value):
	value = value.lstrip('#')
	finalValue = value
	if len(value) == 3:
		finalValue = ''
		for i in value:
			finalValue += i + i
	return list(int(finalValue[i:i+2], 16) for i in (0, 2, 4))
	
def arrToStr(arr):
	res = "["
	l = len(arr)
	for i in range(l):
		res += arr[i]
		if i < l-1:
			res += ","
	res += "]"
	return res