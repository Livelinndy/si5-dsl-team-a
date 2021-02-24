from pyCinEditorML.kernel.Clips import Video, Blank, Concat

VIDEO = 0
BLANK = 1
CONCAT = 2

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
		self.temporal = None
		self.clipList = None

	def on_color(self, color):
		self.color = color
		self.kind = BLANK
		
	def on_duration(self, temporal):
		self.temporal = temporal
		
	def on_path(self, path):
		self.path = path
		self.kind = VIDEO

	def on_concat(self, clipList):
		self.clipList = clipList
		self.kind = CONCAT

	def get_contents(self):
		"""
		Builds the clip

		:return: Clip, the clip
		"""
		if self.kind == VIDEO:
			return Video(self.name, self.path, self.temporal)
		elif self.kind == BLANK:
			return Blank(self.name, self.color, self.temporal)
		elif self.kind == CONCAT:
			return Concat(self.name, self.clipList, self.temporal)
		else:
			return Blank(self.name, self.color, self.temporal)
		return None
