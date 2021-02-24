import moviepy.editor as mp
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.0.11-Q16\\magick.exe"})

# all videos must be the same size in order to concatenate without errors
defaultVideoSize = (256,144)

# clip c1 color #fff background during 10s 
c1 = mp.ColorClip(size=defaultVideoSize, color=[255,255,255], duration=10)

# add title "FROGS" to c1
tc = mp.TextClip("FROGS", fontsize=75, color='red')
tc = tc.set_pos('center').set_duration(9)
c1 = mp.CompositeVideoClip([c1, tc])

# clip c2 is "frogs.mp4"
c2 = mp.VideoFileClip("../pyCinEditorML/resources/videos/frogs.mp4").resize(newsize=defaultVideoSize)

# concat c1 and c2 to cf
cf =  mp.concatenate_videoclips([c1, c2])

# export cf as "newname.mp4"
cf.write_videofile("newname.mp4", fps=30)

c1.close()
c2.close()
cf.close()
