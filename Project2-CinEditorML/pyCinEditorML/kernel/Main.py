"""
no DSL version of the demo application
"""
import sys
sys.path.append('../')

def demo():
	from kernel.App import App
	from kernel.Clips import Video, Blank
	from kernel.Actions import Action, AddText, Concatenate, \
		ConcatenateWithTransition, Cut, Superpose, Export

	from kernel.Utils import timeToSeconds
	from kernel.Temporal import Temporal

	app = App('main')
	"""frogs_video = Video(
		'frogs_video',
		Temporal('40s', 0, '46s'),
		'frogs.mp4')"""
	# 13s
	iphone_video = Video('iphone_video', Temporal('27s', 24, '37s'), 'iphone7.mp4')
	mario_video = Video('mario_video', Temporal('0s', 3, '3s'), 'hotel_mario.mp4')
	final_video = ConcatenateWithTransition([iphone_video, mario_video])\
		.concatenateWithFadeTransition()
	# final_video = Concatenate([iphone_video, mario_video]).execute()
	Export(final_video, 'final_output.mp4').execute()

	# clipColor = Blank("black_clip", Temporal('1m35s', 14), "#fff")
	# print(clipColor.get_temporal())
	# todo


if __name__ == '__main__':
	demo()
