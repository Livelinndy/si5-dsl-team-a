import sys
import abc
import os
sys.path.append('../')
import moviepy.editor as mp
from moviepy.config import change_settings

if sys.platform != 'linux':
	change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.0.11-Q16\\magick.exe"})
else:
	change_settings({"IMAGEMAGICK_BINARY": r"/usr/bin/magick"})

from kernel.Clips import *



class Action(abc.ABC): # Abstraction for actions on clips	
	@abc.abstractmethod
	def execute(self):
		pass

		
		
class ActionOnClip(Action):
	def __init__(self, clip):
		self.clip = clip.content


		
class AddText(ActionOnClip):
	def __init__(self, clip, duration, text, start_after = 0, text_color = 'red', font_size = 20, pos_x = 'center', pos_y = 'center'):
		super().__init__(clip)
		self.text = text
		self.text_color = text_color
		self.font_size = font_size
		self.position = (pos_x, pos_y)
		self.duration = duration
		self.start_after = start_after
		
	def execute(self): # Add text to clip, return final clip
		tc = mp.TextClip(self.text, fontsize = self.font_size, stroke_color = self.text_color, stroke_width = 1.5)
		tc = tc.set_pos(self.position).set_duration(self.duration).set_start(t = self.start_after)
		return mp.CompositeVideoClip([self.clip, tc])

		
		
class Concatenate(Action):
	def __init__(self, clips):
		self.clips = list(map(lambda v: v.content, clips))

	def execute(self): # Concatenate, return final clip
		return mp.concatenate_videoclips(self.clips)


		
# transition enum
FADE = 0
SLIDE = 1
	
class ConcatenateWithTransition(Concatenate):
	def __init__(self, clips, transition=FADE):
		super().__init__(clips)
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
		
	def execute(self): # Concatenate with transition, return final clip
		return self.concatenateWithSlideTransition() if self.transition == SLIDE else \
			self.concatenateWithFadeTransition()
		
		
		
class Cut(ActionOnClip):
	def __init__(self, clip, from_sec, to_sec):
		self.clip = clip
		self.from_sec = from_sec
		self.to_sec = to_sec
		
	def execute(self): # Cut clip, return final clip
		return self.clip.subclip(self.from_sec, self.to_sec)
		
		
		
class Superpose(ActionOnClip):
	def __init__(self, main_clip, side_clip, pos_x = 'right', pos_y = 'bottom', ratio = 0.30):
		super().__init__(main_clip)
		self.side_clip = side_clip
		self.position = (pos_x, pos_y)
		self.ratio = ratio
		
	def execute(self): # Superpose clip, return final clip
		return mp.CompositeVideoClip([self.main_clip, self.side_clip.resize(self.ratio).set_position(self.position)])
	

	
class Export(Action):
	def __init__(self, content, filename = 'res.mp4', fps = 30):
		self.content = content
		self.filename = filename
		self.fps = fps
		
	def execute(self):
		return self.content.write_videofile(os.path.join('../output', self.filename), self.fps)
