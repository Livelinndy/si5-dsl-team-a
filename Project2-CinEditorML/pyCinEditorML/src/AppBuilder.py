from pyCinEditorML.kernel.App import App
from pyCinEditorML.src.ClipBuilder import ClipBuilder
from pyCinEditorML.src.ActionBuilder import ActionBuilder
from pyCinEditorML.src.TemporalBuilder import TemporalBuilder

# pas encore complet

class AppBuilder:
	"""
	Builder for the application
	"""

	def __init__(self, name, array):
		self.array = array
		self.name = name # app name
		self.clips = []  # List[ClipBuider], builders for the clips
		self.actions = []  # List[ActionBuilder], builders for the actions

	def processData(self):
		if len(self.array) > 0:
			elem = array[0].lower()
			if elem == 'clip':
				self.array.pop(0)
				self.clipProcessData(self.getNextLineIndex())
			elif elem == 'add':
				self.array.pop(0)
			elif elem == 'concat':
				self.array.pop(0)
			elif elem == 'export':
				self.array.pop(0)

	def clipProcessData(self, i):
		cb = ClipBuilder(self.array.pop(0))
		t = TemporalBuilder()
		i -= 1
		while True:
			print("ok")
			# ajout parsing clipcreation et break quand i = 0

	def getNextLineIndex(self):
		for i in range(1, len(self.array)):
			if self.array[i] in ['clip','add','export','concat']:
				return i
		return len(self.array)