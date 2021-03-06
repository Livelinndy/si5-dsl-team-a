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

from kernel.Utils import timeToSeconds

class Action(abc.ABC): # Abstraction for actions on clips	
	@abc.abstractmethod
	def execute(self):
		pass

				
class ActionOnClip(Action):
	def __init__(self, clip):
		self.clip = clip

		
class AddText(ActionOnClip):
	def __init__(self, clip, duration_str, text, start_at = 'beginning', text_color = 'red', font_size = 20, pos_x = 'center', pos_y = 'center'):
		super().__init__(clip)
		self.text = text
		self.text_color = text_color
		self.font_size = font_size
		self.position = (pos_x, pos_y)
		self.duration = timeToSeconds(duration_str)
		self.start_at = start_at
		
	def execute(self): # Add text to clip, return final clip
		tc = mp.TextClip(self.text, fontsize = self.font_size, stroke_color = self.text_color, stroke_width = 1.5)
		tc = tc.set_pos(self.position).set_duration(self.duration)
		if self.start_at != 'beginning':
			if self.start_at == 'end':
				tc = tc.set_start(t = self.clip.duration - self.duration)
			else:
				tc = tc.set_start(t = timeToSeconds(self.start_at))
		return mp.CompositeVideoClip([self.clip, tc])

			
class Concatenate(Action):
	def __init__(self, clips):
		self.clips = clips

	def execute(self): # Concatenate, return final clip
		return mp.concatenate_videoclips(self.clips)

	
# transition enum
FADE = 0
	
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
		
	def execute(self): # Concatenate with transition, return final clip
		return self.concatenateWithFadeTransition()
		
				
class Cut(ActionOnClip):
	def __init__(self, clip, from_time_str, to_time_str):
		super().__init__(clip)
		self.from_time = timeToSeconds(from_time_str)
		self.to_time = timeToSeconds(to_time_str)
		
	def execute(self): # Cut clip, return final clip
		return self.clip.subclip(self.from_time, self.to_time)
		
			
class Superpose(ActionOnClip):
	def __init__(self, clip, side_clip, pos_x = 'right', pos_y = 'bottom', ratio = 0.30):
		super().__init__(clip)
		self.side_clip = side_clip
		self.position = (pos_x, pos_y)
		self.ratio = ratio
		
	def execute(self): # Superpose clip, return final clip
		return mp.CompositeVideoClip([self.clip, self.side_clip.resize(self.ratio).set_position(self.position)])
	

class Export(ActionOnClip):
	def __init__(self, clip, filename = 'res.mp4', fps = 30):
		super().__init__(clip)
		self.filename = filename
		self.fps = fps
		
	def execute(self):
		return self.clip.write_videofile(os.path.join('../output', self.filename), self.fps)
