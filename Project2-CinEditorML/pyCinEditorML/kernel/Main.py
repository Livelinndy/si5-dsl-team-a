"""
no DSL version of the demo application
"""
import sys
sys.path.append('../')

def demo():
	from kernel.App import App
	from kernel.Clips import Video, Blank
	from kernel.Actions import Action, AddText, AddTitle, AddSubtitle, \
		Concatenate, ConcatenateWithTransition, Cut, SetColor, Superpose, Export
	from kernel.Utils import timeToSeconds
	from kernel.Temporal import Temporal

	app = App('main')
	frogs_video = Video(
		'frogs_video',
		Temporal('40s', 0, '46s'),
		'frogs.mp4')
	print(frogs_video.temporal)
	Export(frogs_video, 'output_frogs.mp4', 30).execute()

	# clipColor = Blank("black_clip", Temporal('1m35s', 14), "#fff")
	# print(clipColor.get_temporal())
	# todo


if __name__ == '__main__':
	demo()
