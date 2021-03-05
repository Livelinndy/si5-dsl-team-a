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
	def __init__(self, clip, text, start, duration, color='red', font_size=20, pos_x='center', pos_y='center'):
		self.clip = clip
		self.text = text
		self.color = color
		self.font_size = font_size
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.start = start
		self.duration = duration
		
	def execute(self):
		"""add text to clip, return final clip"""
		tc = mp.TextClip(self.text, fontsize=self.font_size, stroke_color=self.color, stroke_width=1.5)
		tc = tc.set_pos('center').set_duration(5)
		tc = tc.set_duration(self.duration).set_start(self.start)
		return mp.CompositeVideoClip([self.clip.content, tc])


class Concatenate(Action):
	def __init__(self, clips):
		def take_content(v):
			if type(v) is Video or type(v) is Blank:
				return v.get_content()
			return v
		self.clips = list(map(take_content, clips))

	def execute(self):
		return mp.concatenate_videoclips(self.clips)


# transition enum
FADE = 0
SLIDE = 1


class ConcatenateWithTransition(Action):
	def __init__(self, clips, transition=FADE):
		def take_content(v):
			if type(v) is Video or type(v) is Blank:
				return v.get_content()
			return v
		for i in clips:
			print(i)
		self.clips = list(map(take_content, clips))
		# self.durations = list(map(lambda v: v.duration, clips))
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
		content = self.concatenateWithSlideTransition() if self.transition == SLIDE else \
			self.concatenateWithFadeTransition()
		print(self.durations)
		return content


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
	def __init__(self, clip, filename='res.mp4', fps=30):
		self.clip = clip
		self.filename = filename
		self.fps = fps
		
	def execute(self):
		if type(self.clip) is Video or type(self.clip) is Blank:
			return self.clip.content.write_videofile(
				os.path.join('../output', self.filename), self.fps)
		else:
			return self.clip.write_videofile(
				os.path.join('../output', self.filename), self.fps)
