import sys
import abc
import moviepy.editor as mp
import os
sys.path.append('../')

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
	def __init__(self, name, temporal, filename):
		super().__init__(name, temporal)
		self.filename = filename
		self.defaultVideoSize = (256, 144)
		self.declare()

	def get_temporal(self):
		return self.temporal

	def declare(self):
		self.content = mp.VideoFileClip(
			os.path.join('../resources/videos', self.filename)
		).resize(newsize=self.defaultVideoSize)
		if self.temporal and self.temporal.get_temporalPosition() is not None and self.temporal.get_duration() is not None:
			print('X1')
			self.content = self.content.subclip(
				self.temporal.get_temporalPosition(),
				self.temporal.get_endTime()
			)

class Blank(Clip):
	"""
	An empty clip
	"""
	def __init__(self, name, temporal, color='black'): # by default the background is black
		super().__init__(name, temporal)
		self.temporal = temporal
		self.color = hexToRgb(color) if color.startswith('#') else color
		self.defaultVideoSize = (256, 144)

	def get_temporal(self):
		return self.temporal

	def declare(self):
		"""create background"""
		self.content = mp.ColorClip(
			size=self.defaultVideoSize,
			color=self.color,
			duration=self.temporal.get_duration())
		return

class Concat(Clip): ### ??? HAS NOTHING TO DO HERE ???
	"""
	A clip made with other clips
	"""
	def __init__(self, name, clipList, temporal):
		super().__init__(name, temporal)