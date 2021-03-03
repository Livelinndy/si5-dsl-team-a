import sys
import abc
import moviepy.editor as mp
import os
sys.path.append('../')
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
	def __init__(self, clip):
		self.clip = clip
		
	def execute(self):
		"""execute action"""
		return
		
class AddTitle(AddText):
	def __init__(self, clip):
		self.clip = clip
	
	def execute(self):
		"""execute action"""
		return
		
class AddSubtitle(AddText):
	def __init__(self, clip):
		self.clip = clip
		
	def execute(self):
		"""execute action"""
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
