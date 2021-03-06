#!/usr/bin/python
import re
import sys
sys.path.append('../')
from kernel.AppInit import AppInit
from kernel.Clips import Video, Blank
from kernel.Actions import Action, AddText, \
    Concatenate, ConcatenateWithTransition, Superpose, Export
from Exceptions import UndefinedAction, UndefinedClip, MySyntaxError

"""
DSL version of the demo application
Usage example: Main.py test1
Where "test1" is the name of a .ceml script from the resources folder
"""

def process(line):
    clip_name = None
    clips = None
    filename = None
    begin = None
    end = None
    title_text = None
    clip_name = None
    transition = None
    clip_on_top = None
    clip_beneath = None
    vertical_pos = None
    horizontal_pos = None
    scale = None
    blank_name = None
    duration = None
    rgb_color = None
    text_content = None
    font_size = None
    begin = None
    regexes = {
        'import_video_with_time': re.compile('clip\s+(?P<clip_name>[a-zA-Z0-9]+)\s+is\s+"(?P<filename>[^"]+)"\s+from\s+(?P<begin>[0-9]*h?[0-9]*m?[0-9]+s)\s+to\s+(?P<end>[0-9]*h?[0-9]*m?[0-9]+s)'),
        'import_video': re.compile('clip\s+(?P<clip_name>[a-zA-Z0-9]+)\s+is\s+"(?P<filename>[^"]+)"'),
        'add_text': re.compile('add\s+(?P<text_type>(text|subtitle|title))\s+"(?P<text_content>[^"]+)"\s+(color\s+(?P<rgb_color>#[0-9a-f]+)\s+)?(fontsize\s+(?P<font_size>[0-9]+px)\s+)?to\s+(?P<clip_name>[a-zA-Z0-9]+)(\s+at\s+(?P<begin>[0-9]*h?[0-9]*m?[0-9]+s))?(\s+during\s+(?P<duration>[0-9]*h?[0-9]*m?[0-9]+s))?'),
        'blank': re.compile('clip\s+(?P<blank_name>[a-zA-Z0-9]+)\s+color\s+(?P<rgb_color>#[0-9a-f]+)\s+background\s+during\s+(?P<duration>[0-9]*h?[0-9]*m?[0-9]+s)'),
        'stack':  re.compile('add\s+clip\s+(?P<clip_on_top>[a-zA-Z0-9]+)\s+on\s+(?P<vertical_pos>[a-zA-Z]+)\s+(?P<horizontal_pos>[a-zA-Z]+)\s+scale\s+(?P<scale>[0-9]+.?[0-9]*)\s+to\s+(?P<clip_beneath>[a-zA-Z0-9]+)'),
        'concat_with_transition': re.compile('concat\s+(?P<clips>.+)\s+with\s+transition\s+(?P<transition>[a-zA-Z0-9]+)\s+to\s+(?P<clip_final_name>[a-zA-Z0-9]+)'),
        'concat': re.compile('concat\s+(?P<clips>.+)\s+to\s+(?P<clip_final_name>[a-zA-Z0-9]+)'),
        'export': re.compile('export\s+(?P<clip_name>[a-zA-Z0-9]+)\s+as\s+"(?P<filename>[^"]+)"')
    }
    regex_key = None
    for key, value in regexes.items():
        match = value.match(line)
        if match:
            regex_key = key
            break

    if regex_key == 'import_video':
        clip_name = match.group('clip_name')
        filename = match.group('filename')
        return Video(clip_name, filename)

    if regex_key == 'export':
        clip_name = match.group('clip_name')
        filename = match.group('filename')
        return Export(clip_name, filename)

    if regex_key == 'add_text':
        text_type = match.group('text_type')
        duration = match.group('duration')
        rgb_color = match.group('rgb_color')
        text_content = match.group('text_content')
        font_size = match.group('font_size')
        clip_name = match.group('clip_name')
        begin = match.group('begin')
        if text_type == 'title':
            return AddText(clip_name, text_content, duration, begin, rgb_color, 40)
        elif text_type == 'subtitle':
            return AddText(clip_name, text_content, duration, begin, rgb_color, 20, pos_y = 'bottom')
        else:
            return AddText(clip_name, text_content, duration, begin, rgb_color, font_size)

    if regex_key == 'stack':
        clip_on_top = match.group('clip_on_top')
        clip_beneath = match.group('clip_beneath')
        vertical_pos = match.group('vertical_pos')
        horizontal_pos = match.group('horizontal_pos')
        scale = match.group('scale')
        return Superpose(clip_beneath, clip_on_top, horizontal_pos, vertical_pos, scale)

    if regex_key == 'blank':
        blank_name = match.group('blank_name')
        duration = match.group('duration')
        rgb_color = match.group('rgb_color')
        return Blank(blank_name, duration, rgb_color)

    if regex_key == 'concat' or regex_key == 'concat_with_transition':
        clips_str = match.group('clips')
        clip_name = match.group('clip_final_name')
        if len(clips_str) > 0:
            clips_str = re.split('\s+and\s+', clips_str)
        if regex_key == 'concat':
            return Concatenate(clips_str, clip_name)
        else:
            transition = match.group('transition')
            return ConcatenateWithTransition(clips_str, clip_name, transition)

    if regex_key == 'import_video_with_time':
        clip_name = match.group('clip_name')
        filename = match.group('filename')
        begin = match.group('begin')
        end = match.group('end')
        return Video(clip_name, filename, begin, end)

if len(sys.argv) > 1:
    file = open('../resources/scenarios/' + sys.argv[1] + '.ceml')
    text = file.read()
    file.close()
    actions = [AppInit()]
    lines = re.split('\n+', text)
    for l in lines:
        actions.append(process(l))
    print(actions)
    code = ""
    for a in actions:
        code += a.execute()
    print(code)
    exec(code)
else:
    print("Specify the CEML script name")
