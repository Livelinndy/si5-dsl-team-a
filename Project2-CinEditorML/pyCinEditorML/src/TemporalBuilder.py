from pyCinEditorML.kernel.Temporal import Temporal

# verifier si complet

class TemporalBuilder:
	
	def __init__(self):
		"""
		Constructor.
		"""
		self.startTime = None
		self.duration = None  # string, path for VIDEO
		self.endTime = None # string, background color for BLANK

	def on_duration(self, duration):
		self.duration = duration
	
	def on_end(self, endTime):
		if endTime == 'end':
			endTime = None
		self.endTime = endTime

	def on_start(self, startTime):
		if startTime == 'beginning':
			startTime = None
		self.startTime = startTime

	def get_contents(self):
		"""
		Builds the clip

		:return: Clip, the clip
		"""
		if self.startTime == None:
			self.startTime = '0s'
		if self.duration == None:
			self.duration = '10s'
		return Temporal(self.startTime, self.duration, self.endTime)
