import sys
import abc
sys.path.append('../')

# import Utils
# import moviepy.editor as mp
# from Utils import hexToRgb
# from Temporal import Temporal

from kernel.Utils import *
from kernel.Temporal import Temporal


class Clip(abc.ABC):
	"""
	Abstraction for clips
	"""
	def __init__(self, name, temporal):
		self.temporal = temporal
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
		super().__init__(name, temporal)
		self.path = path
		# set 

	def get_temporal(self):
		return self.temporal

	def declare(self):
		"""open video"""
		return

class Blank(Clip):
	"""
	An empty clip
	"""
	def __init__(self, name, temporal, color='black'): # by default the background is black
		super().__init__(name, temporal)
		self.color = color
		# self.temporal = temporal
		self.color = hexToRgb(color) if color.startswith('#') else color
		self.defaultVideoSize = (256, 144)

	def get_temporal(self):
		return self.temporal

	def declare(self):
		"""create background"""
		self.content = mp.ColorClip(
			size=self.defaultVideoSize, color=self.color, duration=self.temporal.get_duration())
		return

class Concat(Clip):
	"""
	A clip made with other clips
	"""
	def __init__(self, name, clipList, temporal):
		super().__init__(name, temporal)