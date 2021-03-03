# from Utils import *


from pyCinEditor.kernel.Utils import *
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

	def get_duration(self):
		return self.duration

	def __str__(self):
		return str(self.temporalPosition) + '\n' \
			+ str(self.duration)
