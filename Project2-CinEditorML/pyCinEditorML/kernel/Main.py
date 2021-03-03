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

	clip1 = Video(
		"c1",
		Temporal('0s', 14, None),
		"../resources/videos/frogs.mp4")
	print(clip1.get_temporal())

	clipColor = Blank("black_clip", Temporal('1m35s', 14), "#fff")
	print(clipColor.get_temporal())
	# todo

if __name__ == '__main__':
	demo()
