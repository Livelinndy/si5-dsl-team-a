#!/usr/bin/python
import re
import sys
import time
sys.path.append('../')
# from kernel.App import App
from kernel.Clips import Video, Blank
from kernel.Actions import Action, AddText, \
	Concatenate, ConcatenateWithTransition, Cut, Superpose, Export
from kernel.Utils import timeToSeconds
# from kernel.Temporal import Temporal

"""
DSL version of the demo application
Usage example: Main.py test1
Where "test1" is the name of a .ceml script from the resources folder
"""

# pas encore lie avec AppBuilder

### TESTS import
# temporal = Temporal('1m55s', 40)
# print(temporal)


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
		'import_video_with_time': re.compile(
			'clip\s+(?P<clip_name>[a-zA-Z0-9]+)\s+is\s+"(?P<filename>[^"]+)"\s+from\s+(?P<begin>[0-9]*h?[0-9]*m?[0-9]+s)\s+to\s+(?P<end>[0-9]*h?[0-9]*m?[0-9]+s)'),
		'import_video': re.compile('clip\s+(?P<clip_name>[a-zA-Z0-9]+)\s+is\s+"(?P<filename>[^"]+)"'),
		# 'add_title': re.compile('add\s+title\s+"(?P<title_text>[^"]+)"\s+to\s+(?P<clip_name>[a-zA-Z0-9]+)'),

		'add_text': re.compile('add\s+(sub)?title\s+"(?P<text_content>[^"]+)"\s+(color\s+(?P<rgb_color>#[0-9a-f]+)\s+)?(fontsize\s+(?P<font_size>[0-9]+px)\s+)?to\s+(?P<clip_name>[a-zA-Z0-9]+)(\s+at\s+(?P<begin>[0-9]*h?[0-9]*m?[0-9]+s))?(\s+during\s+(?P<duration>[0-9]*h?[0-9]*m?[0-9]+s))?'),
		'blank': re.compile('clip\s+(?P<blank_name>[a-zA-Z0-9]+)\s+color\s+(?P<rgb_color>#[0-9a-f]+)\s+background\s+during\s+(?P<duration>[0-9]*h?[0-9]*m?[0-9]+s)'),
		'stack':  re.compile('add\s+clip\s+(?P<clip_on_top>[a-zA-Z0-9]+)\s+on\s+(?P<vertical_pos>[a-zA-Z]+)\s+(?P<horizontal_pos>[a-zA-Z]+)\s+scale\s+(?P<scale>[0-9]+.?[0-9]*)\s+to\s+(?P<clip_beneath>[a-zA-Z0-9]+)'),
		'concat_with_transition': re.compile(
			'concat\s+(?P<clips>.+)\s+with\s+transition\s+(?P<transition>[a-zA-Z0-9]+)\s+to\s+(?P<clip_final_name>[a-zA-Z0-9]+)'),
		'concat': re.compile('concat\s+(?P<clips>.+)\s+to\s+(?P<clip_final_name>[a-zA-Z0-9]+)'),
		'export': re.compile('export\s+(?P<clip_name>[a-zA-Z0-9]+)\s+as\s+"(?P<filename>[^"]+)"')
	}
	regex_key = None
	for key, value in regexes.items():
		match = value.match(line)
		if match:
			regex_key = key
			break

	if regex_key == 'import_video' or regex_key == 'export':
		clip_name = match.group('clip_name')
		filename = match.group('filename')
		print(clip_name + ' ' + filename)

	if regex_key == 'add_text':
		duration = match.group('duration')
		rgb_color = match.group('rgb_color')
		text_content = match.group('text_content')
		font_size = match.group('font_size')
		clip_name = match.group('clip_name')
		begin = match.group('begin')
		print(f"{text_content} {rgb_color} {font_size} {clip_name} {begin} {duration}")

	if regex_key == 'stack':
		clip_on_top = match.group('clip_on_top')
		clip_beneath = match.group('clip_beneath')
		vertical_pos = match.group('vertical_pos')
		horizontal_pos = match.group('horizontal_pos')
		scale = match.group('scale')
		print(clip_on_top + ' ' + vertical_pos + ' ' + horizontal_pos + ' ' + scale + ' ' + clip_beneath)

	if regex_key == 'blank':
		blank_name = match.group('blank_name')
		duration = match.group('duration')
		rgb_color = match.group('rgb_color')
		print(blank_name + ' ' + rgb_color + ' ' + duration)

	if regex_key == 'concat' or regex_key == 'concat_with_transition':
		clips_str = match.group('clips')
		clip_name = match.group('clip_final_name')
		if len(clips_str) > 0:
			clips_str = re.split('\s+and\s+', clips_str)
		for i in clips_str:
			print(i, end=' ')
		if regex_key == 'concat_with_transition':
			transition = match.group('transition')
			print('| ' + transition, end=' ')
		print('| ' + clip_name)

	if regex_key == 'import_video_with_time':
		clip_name = match.group('clip_name')
		filename = match.group('filename')
		begin = match.group('begin')
		end = match.group('end')
		print(clip_name + ' ' + filename + ' ' + begin + ' ' + end)


start = time.time()
if len(sys.argv) > 1:
	file = open('../resources/scenarios/' + sys.argv[1] + '.ceml')
	text = file.read()
	file.close()
	finalArray = []
	tmp = []
	array = re.split('\n+', text)
	for l in array:
		process(l)
	end = time.time()
	# print(end - start)
	# print(array)
else:
	print("Specify the CEML script name")

"""	for i in array:
		s = re.split('//', i)[0].strip()
		if s != '':
			tmp.append(s)
	isText = False
	tmpText = []
	for i in tmp:
		for j in re.split(' +', i):
			if not isText and j[0] != '"':
				finalArray.append(j)
			elif (not isText and j[0] == '"') or (isText and j[-1] != '"'):
				isText = True
				tmpText.append(j)
			if isText and j[-1] == '"':
				tmpText.append(j)
				finalArray.append(' '.join(tmpText))
				tmpText = []
				isText = False
	print(finalArray)"""
