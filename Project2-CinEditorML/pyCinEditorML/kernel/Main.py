"""
no DSL version of the demo application
"""

def demo():
    from pyCinEditorML.kernel.App import App
	from pyCinEditorML.kernel.Clips import Video, Blank
    from pyCinEditorML.kernel.Actions import Action, AddText, AddTitle, AddSubtitle, Concatenate, ConcatenateWithTransition, Cut, SetColor, Superpose, Export
    from pyCinEditorML.kernel.Utils import timeToSeconds

    clip1 = Video("c1", "../resources/videos/frogs.mp4")
    
	# todo

    print app


if __name__ == '__main__':
    demo()
