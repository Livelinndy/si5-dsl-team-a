"""
no DSL version of the demo application
"""

def demo():
	# from kernel.App import App
	# from kernel.Clips import Video, Blank
	# from kernel.Actions import Action, AddText, AddTitle, AddSubtitle, Concatenate, ConcatenateWithTransition, Cut, SetColor, Superpose, Export
	# from kernel.Utils import timeToSeconds
	# from kernel.Temporal import Temporal

	from pyCinEditorML.kernel.App import App
	from pyCinEditorML.kernel.Clips import Video, Blank
	from pyCinEditorML.kernel.Actions import Action, AddText, AddTitle, AddSubtitle, Concatenate,\
		ConcatenateWithTransition, Cut, SetColor, Superpose, Export
	from pyCinEditorML.kernel.Utils import timeToSecond

	clip1 = Video(
		"c1",
		Temporal('0s', 14, None),
		"../resources/videos/frogs.mp4")
	print(clip1.get_temporal())

	clipColor = Blank("black_clip", Temporal('1m35s', 14, None), "#fff")
	print(clipColor.get_temporal())
	# todo

# 	print app


if __name__ == '__main__':
	demo()
