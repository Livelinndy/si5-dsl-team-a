import sys
import abc
import os
sys.path.append('../')

import moviepy.editor as mp
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.0.11-Q16\\magick.exe"})

from kernel.App import App

# pas encore complet

class Action(abc.ABC):
	"""
	Abstraction for actions over clips
	"""
	def __init__(self, clip):
		self.clip = clip
		
	@abc.abstractmethod
	def execute(self):
		pass

class AddText(Action):
	def __init__(self, clip, text, color = 'red', pos_x = 'center', pos_y = 'center'):
		self.clip = clip
		self.text = text
		self.color = color
		self.pos_x = pos_x
		self.pos_y = pos_y
		
	def execute(self):
		"""execute action"""
		tc = mp.TextClip(self.text, fontsize=75, color)
		tc = tc.set_pos('center').set_duration(9)
		c1 = mp.CompositeVideoClip([c1, tc])
		return


		
class Concatenate(Action):
	def __init__(self, clips):
		self.clips = clips

	def execute(self):
		return mp.concatenate_videoclips(self.clips)
		
class ConcatenateWithTransition(Action):
	# need to add transition argument in constructor
	def __init__(self, clip):
		self.clip = clip
		
	def execute(self):
		"""execute action"""
		return
		
		
		
class Cut(Action):
	def __init__(self, clip):
		self.clip = clip
		
	def execute(self):
		"""execute action"""
		return
		
		
		
class SetColor(Action):
	def __init__(self, clip):
		self.clip = clip
		
	def execute(self):
		"""execute action"""
		return
		
		
		
class Superpose(Action):
	def __init__(self, clip):
		self.clip = clip
		
	def execute(self):
		"""execute action"""
		return
		
		
		
class Export(Action):
	def __init__(self, clip, filename='a.out.mp4', fps=30):
		self.clip = clip
		self.filename = filename
		self.fps = fps
		
	def execute(self):
		return self.clip.content.write_videofile(
			os.path.join('../output', self.filename), self.fps)
