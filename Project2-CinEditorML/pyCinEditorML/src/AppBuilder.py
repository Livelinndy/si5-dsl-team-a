from pyCinEditorML.kernel.App import App
from pyCinEditorML.src.ClipBuilder import ClipBuilder
from pyCinEditorML.src.ActionBuilder import ActionBuilder

# pas encore complet

class AppBuilder:
	"""
	Builder for the application
	"""

	def __init__(self, name):
		self.name = name # app name
		self.clips = []  # List[ClipBuider], builders for the clips
		self.actions = []  # List[ActionBuilder], builders for the actions

	def run(self, array):
		if len(array) > 0:
			elem = array[0].lower()
			if elem == 'clip':
				array.pop(0)
			elif elem == 'add':
				array.pop(0)
			elif elem == 'concat':
				array.pop(0)
			elif elem == 'export':
				array.pop(0)
