"""
no DSL version of the demo application
"""
import sys
sys.path.append('../')

from kernel.Clips import Video, Blank
from kernel.Actions import Action, AddText, Concatenate, \
	ConcatenateWithTransition, FADE, Superpose, Export

from kernel.Utils import timeToSeconds

def scenario1():
	# (a) add a title on a black background at the beginning for 10 seconds
	t1 = Blank('t1', '10s').execute()
	t1 = AddText(t1, 10, 'title: frogs').execute()

	# (b) add a first video clip that appears directly after the title screen
	v1 = Video('c1', 'frogs.mp4').execute()

	# (c) add another video clip that appears directly after the first clip
	v2 = Video('c2', 'frogs2.mp4').execute()

	# (d) add a thanks sentence at the end, lasting for 15 seconds
	v2 = AddText(v2, 15, 'thanks for watching', start_after = (v2.duration - 15)).execute()

	# (e) export the result as a video file
	cf = Concatenate([t1, v1, v2]).execute()
	Export(cf, 's1_kernel.mp4').execute()

def scenario2():
        # (a) add an introduction title on a black background at the beginning for 10 seconds
        t1 = Blank('t1', '10s').execute()
        t1 = AddText(t1, 10, 'introduction title').execute()

        # (b) load a first video clip clip1
        # (c) create two clips clip1a and clip1b respectively taken from 00:23 to 01:47 min and from 02:01 to 02:21 min
        c1a = Video('c1a', 'frogs.mp4', '9s', '1m08s').execute()
        c1b = Video('c1b', 'frogs.mp4', '1m49s', '2m10s').execute()

        # (d) add a subtitle to clip1a from the beginning and for 10 seconds,
        #     followed by another subtitle starting 30 seconds after the end of the first one and visible for 10 seconds
        c1a = AddText(c1a, 10, 'subtitle s1a', pos_y = 'bottom').execute()
        c1a = AddText(c1a, 10, 'subtitle s2a', pos_y = 'bottom', start_after = 40).execute()

        # (e) add clip1b with a subtitle starting 5 seconds before clip1b and lasting for 15 seconds.
        c1b = AddText(c1b, 15, 'subtitle s1b', pos_y = 'bottom', start_after = -5).execute()

        # (f) add a thanks conclusive text on a fixed background color (let’s say black).
        t2 = Blank('t1', '10s').execute()
        t2 = AddText(t2, 10, 'thanks for watching').execute()

        # (g) export the result as a video file
        cf = Concatenate([t1, c1a, c1b, t2]).execute()
        Export(cf, 's2_kernel.mp4').execute()

def scenario3():
        # (a) add fade out fade in transitions when creating the main video
        c1side = Video('c1side', 'frogs.mp4', '33s', '1m05s').execute()
        c1a = Video('c1a', 'frogs.mp4', '9s', '22s').execute()
        c1b = Video('c1b', 'frogs.mp4', '1m33s', '1m45s').execute()
        c1c = Video('c1c', 'frogs.mp4', '2m03s', '2m10s').execute()
        c1main = ConcatenateWithTransition([c1a, c1b, c1c], FADE).execute()

        # (b) stack a side video over the main video in the corner
        cf = Superpose(c1main, c1side).execute()

        # (c) export the result as a video file
        Export(cf, 's3_kernel.mp4').execute()

if __name__ == '__main__':
        #scenario1()
        #scenario2()
        scenario3()
        
