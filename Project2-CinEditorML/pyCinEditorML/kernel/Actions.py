import sys
import abc
sys.path.append('../')

from kernel.Utils import timeToSeconds, arrToStr

class Action(abc.ABC): # Abstraction for actions on clips	
	@abc.abstractmethod
	def execute(self):
		pass

				
class ActionOnClip(Action):
	def __init__(self, clip_name):
		self.clip_name = clip_name

		
class AddText(ActionOnClip):
	def __init__(self, clip_name, duration_str, text, start_at = 'beginning', text_color = 'red', font_size = 20, pos_x = 'center', pos_y = 'center'):
		super().__init__(clip_name)
		self.text = text
		self.text_color = 'red' if text_color is None else text_color
		self.font_size = 20 if font_size is None else font_size
		self.position = ('center', 'center') if (pos_x is None or pos_y is None) else (pos_x, pos_y)
		self.duration = timeToSeconds(duration_str)
		self.start_at = 'beginning' if start_at is None else start_at
		
	def execute(self): # Add text to clip, return final clip
		res = "tc = mp.TextClip('" + self.text + "', fontsize = " + str(self.font_size) + ", stroke_color = '" + self.text_color + "', stroke_width = 1.5)\n"
		res += "tc = tc.set_pos(" + str(self.position) + ").set_duration(" + str(self.duration) + ")\n"
		if self.start_at != 'beginning':
			res += "tc = tc.set_start(t = " + str(timeToSeconds(self.start_at)) + ")\n"
		res += self.clip_name + " = mp.CompositeVideoClip([" + self.clip_name + ", tc])\n"
		return res

			
class Concatenate(Action):
	def __init__(self, clip_names, dest):
		self.clip_names = clip_names
		self.dest = dest

	def execute(self): # Concatenate, return final clip
		res = self.dest + " = mp.concatenate_videoclips(" + arrToStr(self.clip_names) + ")\n"
		return res

	
# transition enum
FADE = 0
	
class ConcatenateWithTransition(Concatenate):
	def __init__(self, clip_names, dest, transition=FADE):
		super().__init__(clip_names, dest)
		self.transition = FADE if transition is None else transition
		
	def concatenateWithFadeTransition(self):
		res = "fadeTime = 2.5\n"
		res += "clipsToConcat = " + arrToStr(self.clip_names) + "\n"
		res += "clipsWithParams = [clipsToConcat[0]]\n"
		res += "idx = clipsToConcat[0].duration - fadeTime\n"
		res += "for video in clipsToConcat[1:]:\n"
		res += "	clipsWithParams.append(video.set_start(idx).crossfadein(fadeTime))\n"
		res += "	idx += video.duration - fadeTime\n"
		res += self.dest + " = mp.CompositeVideoClip(clipsWithParams)\n"
		return res
		
	def execute(self): # Concatenate with transition, return final clip
		return self.concatenateWithFadeTransition()
		
				
class Cut(ActionOnClip):
	def __init__(self, clip_name, from_time_str, to_time_str):
		super().__init__(clip_name)
		self.from_time = timeToSeconds(from_time_str)
		self.to_time = timeToSeconds(to_time_str)
		
	def execute(self): # Cut clip, return final clip
		res = self.clip_name + ".subclip(" + str(self.from_time) + ", " + str(self.to_time) + ")\n"
		return res
		
			
class Superpose(ActionOnClip):
	def __init__(self, clip_name, side_clip_name, pos_x = 'right', pos_y = 'bottom', ratio = 0.30):
		super().__init__(clip_name)
		self.side_clip_name = side_clip_name
		self.position = ('center', 'center') if (pos_x is None or pos_y is None) else (pos_x, pos_y)
		self.ratio = 0.30 if ratio is None else ratio
		
	def execute(self):
		res = self.clip_name + " = mp.CompositeVideoClip([" + self.clip_name + ", " + self.side_clip_name + ".resize(" + str(self.ratio) + ").set_position(" + str(self.position) + ")])\n"
		return res
	

class Export(ActionOnClip):
	def __init__(self, clip_name, filename = 'res.mp4', fps = 30):
		super().__init__(clip_name)
		self.filename = filename
		self.fps = fps
		
	def execute(self):
		res = self.clip_name + ".write_videofile(os.path.join('../output', '" + self.filename + "'), " + str(self.fps) + ")\n"
		return res
