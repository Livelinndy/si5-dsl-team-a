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
	def __init__(self, clip, text, color = 'red', font_size=20, pos_x='center', pos_y='center'):
		self.clip = clip
		self.text = text
		self.color = color
		self.font_size = font_size
		self.pos_x = pos_x
		self.pos_y = pos_y
		
	def execute(self):
		"""add text to clip, return final clip"""
		tc = mp.TextClip(self.text, fontsize=self.font_size, stroke_color=self.color, stroke_width=1.5)
		tc = tc.set_pos('center').set_duration(9)
		return mp.CompositeVideoClip([self.clip, tc])

class Concatenate(Action):
	def __init__(self, clips):
		self.clips = list(map(lambda v: v.get_content(), clips))

	def execute(self):
		return mp.concatenate_videoclips(self.clips)


# transition enum
FADE = 0
SLIDE = 1
	
class ConcatenateWithTransition(Action):
	def __init__(self, clips, transition=FADE):
		self.clips = list(map(lambda v: v.get_content(), clips))
		self.transition = transition
		
	def concatenateWithFadeTransition(self):
		fadeTime = 2.5
		clipsToConcat = self.clips
		clipsWithParams = [clipsToConcat[0]]
		idx = clipsToConcat[0].duration - fadeTime
		for video in clipsToConcat[1:]:
			clipsWithParams.append(video.set_start(idx).crossfadein(fadeTime))
			idx += video.duration - fadeTime
		return mp.CompositeVideoClip(clipsWithParams)
		
	def concatenateWithSlideTransition(self):
		# TODO
		pass
		
	def execute(self):
		"""concatenate with transition, return final clip"""
		return self.concatenateWithSlideTransition() if self.transition == SLIDE else \
			self.concatenateWithFadeTransition()
		
class Cut(Action):
	def __init__(self, clip, from_sec, to_sec):
		self.clip = clip
		self.from_sec = from_sec
		self.to_sec = to_sec
		
	def execute(self):
		"""cut clip, returns final clip"""
		return self.clip.subclip(self.from_sec, self.to_sec)
		
class Superpose(Action):
	def __init__(self, main_clip, side_clip, pos_x='right', pos_y='bottom', ratio=0.30):
		self.main_clip = main_clip
		self.side_clip = side_clip
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.ratio = ratio
		
	def execute(self):
		"""superpose clip, return final clip"""
		return mp.CompositeVideoClip([self.main_clip, self.side_clip.resize(self.ratio).set_position((self.pos_x, self.pos_y))])
			
class Export(Action):
	def __init__(self, clip, filename='res.mp4', fps = 30):
		self.clip = clip
		self.filename = filename
		self.fps = fps
		
	def execute(self):
		return self.clip.write_videofile(
			os.path.join('../output', self.filename), self.fps)
