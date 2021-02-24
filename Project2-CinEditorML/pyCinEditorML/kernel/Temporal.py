from pyCinEditorML.kernel.Utils import *

class Temporal:
	"""
	time linked to clips
	"""
	def __init__(self, startTime, duration, endTime = None):
		self.temporalPosition = timeToSeconds(startTime)
		if endTime != None:
			self.duration = timeBetween(startTime, endTime)
		else:
			self.duration = duration