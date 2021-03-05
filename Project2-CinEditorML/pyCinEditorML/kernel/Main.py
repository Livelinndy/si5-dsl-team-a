"""
no DSL version of the demo application
"""
import sys
sys.path.append('../')

from kernel.App import App
from kernel.Clips import Video, Blank
from kernel.Actions import Action, AddText, Concatenate, \
	ConcatenateWithTransition, Cut, Superpose, Export

from kernel.Utils import timeToSeconds

def test():
	app = App('main')
	"""frogs_video = Video(
		'frogs_video',
		Temporal('40s', 0, '46s'),
		'frogs.mp4')"""

	iphone_video = Video('iphone_video', Temporal('27s', 24, '37s'), 'iphone7.mp4')
	intro_video = Blank('blank_video', Temporal('0s', 5, '5s'), '#000')
	intro_video = AddText(intro_video, 'An Iphone Video', 2, 3).execute()
	# mario_video = Video('mario_video', Temporal('0s', 3, '3s'), 'hotel_mario.mp4')
	# final_video = ConcatenateWithTransition([iphone_video, mario_video])\
	# .concatenateWithFadeTransition()
	# final_video = Concatenate([iphone_video, mario_video]).execute()
	final_video = ConcatenateWithTransition([intro_video, iphone_video]).concatenateWithFadeTransition()
	Export(final_video, 'final_output.mp4').execute()

	# clipColor = Blank("black_clip", Temporal('1m35s', 14), "#fff")
	# print(clipColor.get_temporal())
	# todo

def scenario1():
	# (a) add a title on a black background at the beginning for 10 seconds stating where they were and when.
	t1 = Blank('t1', '10s')
	t1.content = AddText(t1, 10, 'title').execute()
	# (b) add a first video clip that appears directly after the title screen
	v1 = Video('c1', 'frogs.mp4')
	# (c) add another video clip that appears directly after the first clip
	v2 = Video('c1', 'frogs2.mp4')
	# (d) add a thanks sentence at the end, lasting for 15 seconds
	t2 = Blank('t1', '10s')
	t2.content = AddText(t2, 10, 'thanks').execute()
	concat_content = Concatenate([t1, v1, v2, t2]).execute()
	# (e) export the result as a video file
	Export(concat_content, 's1_kernel.mp4').execute()
	

if __name__ == '__main__':
	scenario1()
