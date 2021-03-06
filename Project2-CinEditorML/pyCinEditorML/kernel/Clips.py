import sys
import abc
import moviepy.editor as mp
import os
sys.path.append('../')

from kernel.Utils import timeToSeconds, hexToRgb


DEFAULT_VIDEO_SIZE = (256, 144) #(1280, 720)


class Clip(abc.ABC): # Abstraction for clips
	def __init__(self, variable_name):
		self.variable_name = variable_name
	
	@abc.abstractmethod
	def execute(self):
		pass
		
				
class Video(Clip): # A video loaded from file
	def __init__(self, variable_name, filename, from_time_str = None, to_time_str = None):
		super().__init__(variable_name)
		self.filename = filename
		self.from_time = None if (from_time_str is None) else timeToSeconds(from_time_str)
		self.to_time = None if (to_time_str is None) else timeToSeconds(to_time_str)
		
	def execute(self):
		res = self.variable_name + " = mp.VideoFileClip(os.path.join('../resources/videos', '" + self.filename + "')).resize(newsize = " + str(DEFAULT_VIDEO_SIZE) + ")"
		if (self.from_time is not None) and (self.to_time is not None):
			res +=  ".subclip(" + str(self.from_time) + ", " + str(self.to_time) + ")"
		res += "\n"
		return res

		
class Blank(Clip): # An empty clip with colored background
	def __init__(self, variable_name, duration_str, background_color='#000'): # by default the background is black
		super().__init__(variable_name)
		self.duration = timeToSeconds(duration_str)
		self.background_color = hexToRgb(background_color) if background_color.startswith('#') else background_color
		
	def execute(self):
		res = self.variable_name + " = mp.ColorClip(size = " + str(DEFAULT_VIDEO_SIZE) + ", color = " + str(self.background_color) + ", duration = " + str(self.duration) + ")\n"
		return res
