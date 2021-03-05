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
		self.content = None

	def get_content(self):
		return self.content
	
	def set_content(self, content):
		self.content = content
		
		
		
class Video(Clip): # A video loaded from file
	def __init__(self, variable_name, filename):
		super().__init__(variable_name)
		self.filename = filename
		super().set_content(mp.VideoFileClip(os.path.join('../resources/videos', self.filename)).resize(newsize = DEFAULT_VIDEO_SIZE))
		


class Blank(Clip): # An empty clip with colored background
	def __init__(self, variable_name, duration_str, background_color='#fff'): # by default the background is black
		super().__init__(variable_name)
		self.duration = timeToSeconds(duration_str)
		self.background_color = hexToRgb(background_color) if background_color.startswith('#') else background_color
		super().set_content(mp.ColorClip(size = DEFAULT_VIDEO_SIZE, color = self.background_color, duration = self.duration))
