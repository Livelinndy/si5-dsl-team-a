import moviepy.editor as mp
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.0.11-Q16\\magick.exe"})

vf = "../../pyCinEditorML/resources/videos/"

# all videos must be the same size in order to concatenate without errors
ds = (256,144)

# clip c1 is "frogs.mp4" from 33s to 1m11s
c1 = mp.VideoFileClip(vf + "frogs.mp4").resize(newsize=ds).subclip(33, 66)

# clip c2 is "frogs.mp4" from 9s to 22s
c2 = mp.VideoFileClip(vf + "frogs.mp4").resize(newsize=ds).subclip(9, 22)

# clip c3 is "frogs.mp4" from 1m33s to 1m46s
c3 = mp.VideoFileClip(vf + "frogs.mp4").resize(newsize=ds).subclip(93, 106)

# clip c4 is "frogs.mp4" from 2m03s to 2m10s
c4 = mp.VideoFileClip(vf + "frogs.mp4").resize(newsize=ds).subclip(123, 130)

# concat c2 and c3 and c4 with transition fade to cf
fadeTime = 1.5
clipsToConcat = [c2, c3, c4]
clipsWithParams = [clipsToConcat[0]]
idx = clipsToConcat[0].duration - fadeTime
for video in clipsToConcat[1:]:
    clipsWithParams.append(video.set_start(idx).crossfadein(fadeTime))
    idx += video.duration - fadeTime
cf = mp.CompositeVideoClip(clipsWithParams)

# add clip c1 on bottom right scale 0.3 to cf
cf = mp.CompositeVideoClip([cf, c1.resize(0.30).set_position(("right", "bottom"))])

# export cf as "res3.mp4"
cf.write_videofile("res3.mp4", fps=30)

c1.close()
c2.close()
c3.close()
c4.close()
cf.close()
