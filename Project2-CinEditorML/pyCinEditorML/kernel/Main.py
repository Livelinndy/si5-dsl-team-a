""" no DSL version of the demo application """
import sys
sys.path.append('../')

from kernel.AppInit import AppInit
from kernel.Clips import Video, Blank
from kernel.Actions import Action, AddText, Concatenate, \
    ConcatenateWithTransition, FADE, Superpose, Export

from kernel.Utils import timeToSeconds

        
def scenario1():
        actions = [AppInit(),
                   # (a) add a title on a black background at the beginning for 10 seconds
                   Blank('t1', '10s'),
                   AddText('t1', '10s', 'title: frogs'),
                   # (b) add a first video clip that appears directly after the title screen
                   Video('c1', 'frogs.mp4'),
                   # (c) add another video clip that appears directly after the first clip
                   Video('c2', 'frogs2.mp4'),
                   # (d) add a thanks sentence at the end, lasting for 15 seconds
                   AddText('c2', '15s', 'thanks for watching', start_at = '1m55s'),
                   # (e) export the result as a video file
                   Concatenate(['t1', 'c1', 'c2'], 'cf'),
                   Export('cf', 's1_kernel.mp4')]
        code = ""
        for a in actions:
                code += a.execute()
        print(code)
        #exec(code)

def scenario2():
    actions = [AppInit(),
                   # (a) add an introduction title on a black background at the beginning for 10 seconds
                   Blank('t1', '10s'),
                   AddText('t1', '10s', 'introduction title'),
                   # (b) load a first video clip clip1
                   # (c) create two clips clip1a and clip1b respectively taken from 00:23 to 01:47 min and from 02:01 to 02:21 min
                   Video('c1a', 'frogs.mp4', '9s', '1m08s'),
                   Video('c1b', 'frogs.mp4', '1m49s', '2m10s'),
                   # (d) add a subtitle to clip1a from the beginning and for 10 seconds,
                   #     followed by another subtitle starting 30 seconds after the end of the first one and visible for 10 seconds
                   AddText('c1a', '10s', 'subtitle s1a', pos_y = 'bottom'),
                   AddText('c1a', '10s', 'subtitle s2a', pos_y = 'bottom', start_at = '40s'),
                   # (e) add clip1b with a subtitle starting 5 seconds before clip1b and lasting for 15 seconds.
                   AddText('c1b', '15s', 'subtitle s1b', pos_y = 'bottom'),
                   # (f) add a thanks conclusive text on a fixed background color (let’s say black).
                   Blank('t2', '10s'),
                   AddText('t2', '10s', 'thanks for watching'),
                   # (g) export the result as a video file
                   Concatenate(['t1', 'c1a', 'c1b', 't2'], 'cf'),
                   Export('cf', 's2_kernel.mp4')]
    code = ""
    for a in actions:
        code += a.execute()
    print(code)
    #exec(code)

def scenario3():
        actions = [AppInit(),
                   # (a) add fade out fade in transitions when creating the main video
                   Video('c1side', 'frogs.mp4', '33s', '1m05s'),
                   Video('c1a', 'frogs.mp4', '9s', '22s'),
                   Video('c1b', 'frogs.mp4', '1m33s', '1m45s'),
                   Video('c1c', 'frogs.mp4', '2m03s', '2m10s'),
                   ConcatenateWithTransition(['c1a', 'c1b', 'c1c'], 'cf', FADE),
                   # (b) stack a side video over the main video in the corner
                   Superpose('cf', 'c1side'),
                   # (c) export the result as a video file
                   Export('cf', 's3_kernel.mp4')]
        code = ""
        for a in actions:
                code += a.execute()
        print(code)
        #exec(code)

def demoVideo():
        actions = [AppInit(),
                   # (a) add fade out fade in transitions when creating the main video
                   Blank('t1', '10s'),
                   AddText('t1', '10s', 'introduction title'),
                   Video('c1side', 'frogs.mp4', '33s', '1m05s'),
                   Video('c1a', 'frogs.mp4', '9s', '22s'),
                   Video('c1b', 'frogs.mp4', '1m33s', '1m45s'),
                   Video('c1c', 'frogs.mp4', '2m03s', '2m10s'),
                   AddText('c1a', '10s', 'Wow, what a nice frog', pos_y = 'bottom'),
                   AddText('c1c', '10s', 'Wow, what a nice frog', pos_y = 'bottom'),
                   ConcatenateWithTransition(['t1','c1a', 'c1b', 'c1c'], 'cf', FADE),
                   # (b) stack a side video over the main video in the corner
                   Superpose('cf', 'c1side'),
                   # (c) export the result as a video file
                   Export('cf', 'final_demo.mp4')]
        code = ""
        for a in actions:
                code += a.execute()
        print(code)
        exec(code)

if __name__ == '__main__':
    scenario1()
    scenario2()
    scenario3()
    demoVideo()
        
