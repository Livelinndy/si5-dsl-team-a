import abc
import pyCinEditorML.kernel.Utils
from pyCinEditorML.kernel.Temporal import Temporal

class Clip(abc.ABC):
	"""
	Abstraction for clips
	"""
	def __init__(self, name, temporal):
		self.temporat = temporal
		self.name = name
		self.content = None

	@abc.abstractmethod
	def declare(self):
		"""open or create clip"""
		pass

class Video(Clip):
	"""
	A video
	"""
	def __init__(self, name, temporal, path):
		super().__init__(self, name, temporal)
		self.path = path
		# set 

	def declare(self):
		"""open video"""
		return

class Blank(Clip):
	"""
	An empty clip
	"""
	def __init__(self, name, temporal, color = 'black'): # by default the background is black
		super().__init__(self, name, temporal)
		self.color = color

	def declare(self):
		"""create background"""
		return

class Concat(Clip):
	"""
	A clip made with other clips
	"""
	def __init__(self, name, clipList, temporal):
		super().__init__(name, temporal)