import moviepy.editor as mp
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.0.11-Q16\\magick.exe"})

# all videos must be the same size in order to concatenate without errors
defaultVideoSize = (256,144)

# clip c1 color #fff background
# (the default duration is 10s)
c1 = mp.ColorClip(size=defaultVideoSize, color=[255,255,255], duration=10)

# clip c2 is "frogs.mp4" from 9s to 22s
c2 = mp.VideoFileClip("../../pyCinEditorML/resources/videos/frogs.mp4").resize(newsize=defaultVideoSize).subclip(9, 22)

# add title "frogs" to c1
t1 = mp.TextClip("frogs", fontsize=75, color='red')
t1 = t1.set_pos('center').set_duration(10)
c1 = mp.CompositeVideoClip([c1, t1])

# add subtitle "frog sounds" color #f0f fontsize 20px to c2 at 2s during 10s
t2 = mp.TextClip("frog sounds", fontsize=20, color='#ff00ff') # ATTENTION TextClip doesn't accept RGB like ColorClip, but it accepts hex color
t2 = t2.set_pos('bottom').set_duration(10).set_start(t=2)
c2 = mp.CompositeVideoClip([c2, t2])

# concat c1 and c2 to cf
cf =  mp.concatenate_videoclips([c1, c2])

# export cf as "res2.mp4"
cf.write_videofile("res2.mp4", fps=30)

t1.close()
t2.close()
c1.close()
c2.close()
cf.close()
