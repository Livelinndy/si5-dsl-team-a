from pyCinEditorML.kernel.Clips import Video, Blank

VIDEO = 0
BLANK = 1

# verifier si complet

class ClipBuilder:
	
	def __init__(self, name):
		"""
		Constructor.

		:param name: Int, name of the clip
		:param kind: kind of clip to build
		:return:
		"""
		self.name = name
		self.path = None  # string, path for VIDEO
		self.color = None # string, background color for BLANK
		self.kind = None
		self.startTime = None
		self.duration = None # duration for BLANK
		self.endTime = None

	def on_color(self, color):
		self.color = color
		self.kind = BLANK
		
	def on_duration(self, startTime, duration, endTime):
		self.startTime = startTime
		self.duration = duration
		self.endTime = endTime
		
	def on_path(self, path):
		self.path = path
		self.kind = VIDEO

	def get_contents(self):
		"""
		Builds the clip

		:return: Clip, the clip
		"""
		if self.kind == VIDEO:
			return Video(self.name, self.path, self.startTime, self.duration, self.endTime)
		elif self.kind == BLANK:
			return Blank(self.name, self.color, self.startTime, self.duration, self.endTime)
		else:
			return Blank(self.name, self.color, self.startTime, self.duration, self.endTime)
		return None
