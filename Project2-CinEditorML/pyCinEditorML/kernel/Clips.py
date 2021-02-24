import abc
import pyCinEditorML.kernel.Utils
from pyCinEditorML.kernel.Temporal import Temporal

class Clip(abc.ABC):
	"""
	Abstraction for clips
	"""
	def __init__(self, name, startTime, duration, endTime):
		self.timeDuration = Temporal(startTime, duration, endTime)
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
	def __init__(self, name, path, startTime, duration, endTime):
		super().__init__(self, name, startTime, duration, endTime)
		self.path = path
		# set 

	def declare(self):
		"""open video"""
		return

class Blank(Clip):
	"""
	An empty clip
	"""
	def __init__(self, name, color = 'black', startTime = '0s', duration = '15s', endTime = None): # by default the background is black
		super().__init__(self, name, startTime, duration, endTime)
		self.color = color

	def declare(self):
		"""create background"""
		return

class Concat(Clip):
	"""
	A clip made with other clips
	"""
	def __init__(self, name, clipList):
		super().__init__(name, '0s', duration, endTime)