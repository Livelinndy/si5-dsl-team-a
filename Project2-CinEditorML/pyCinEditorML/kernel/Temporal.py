import sys
sys.path.append('../')
from kernel.Utils import *

class Temporal:
	"""
	time linked to clips
	"""
	def __init__(self, startTime='Os', duration=5, endTime=None):
		self.temporalPosition = timeToSeconds(startTime)
		if endTime is not None:
			self.duration = timeBetween(startTime, endTime)
		else:
			self.duration = duration
		self.endTime = timeToSeconds(endTime) if endTime is not None else endTime
		print(f'duration={self.duration}')
		print(self.__str__())

	def get_duration(self):
		return self.duration

	def get_temporalPosition(self):
		return self.temporalPosition

	def get_endTime(self):
		return self.endTime

	def __str__(self):
		return f'temporalPosition: {self.temporalPosition}\nduration: {self.duration}\nendTime: {self.endTime}'
