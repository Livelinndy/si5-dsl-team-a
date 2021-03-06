#!/usr/bin/python
import re
import sys
import time
sys.path.append('../')
from kernel.Clips import Video, Blank
from kernel.Actions import Action, AddText, \
	Concatenate, ConcatenateWithTransition, Superpose, Export

"""
DSL version of the demo application
Usage example: Main.py test1
Where "test1" is the name of a .ceml script from the resources folder
"""


"""def process(line):
	clip_name = None
	clips = None
	filename = None
	begin = None
	end = None
	title_text = None
	clip_name = None
	transition = None
	regexes = {
		'import_video_with_time': re.compile(
			'clip\s+(?P<clip_name>[a-zA-Z0-9]+)\s+is\s+"(?P<filename>[^"]+)"\s+from\s+(?P<begin>[0-9]*h?[0-9]*m?[0-9]+s)\s+to\s+(?P<end>[0-9]*h?[0-9]*m?[0-9]+s)'),
		'import_video': re.compile('clip\s+(?P<clip_name>[a-zA-Z0-9]+)\s+is\s+"(?P<filename>[^"]+)"'),
		'add_title': re.compile('add\s+title\s+"(?P<title_text>[^"]+)"\s+to\s+(?P<clip_name>[a-zA-Z0-9]+)'),

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

	if regex_key == 'concat' or regex_key == 'concat_with_transition':
		clips_str = match.group('clips')
		clip_name = match.group('clip_final_name')
		if len(clips_str) > 0:
			clips_str = re.split('\s+and\s+', clips_str)
		for i in clips_str:
			print(i, end = " ")
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

	if regex_key == 'add_title':
		title_text = match.group('title_text')
		clip_name = match.group('clip_name')
		print(title_text + ' ' + clip_name)"""



def getSequenceOfActions(lines):
	for line in lines:
		line = line.strip() # strips the newline character
		count += 1
		print("Line{}: {}".format(count, line))


if len(sys.argv) > 1:
	file = open('../resources/scenarios/' + sys.argv[1] + '.ceml', 'r')
	text = file.read()
	file.close()
	finalArray = []
	tmp = []
	array = re.split('\n+', text)

	for i in array:
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
			elif isText and j[-1] == '"':
				tmpText.append(j)
				finalArray.append(' '.join(tmpText))
				tmpText = []
				isText = False
	print(finalArray)

	end = time.time()
	# print(end - start)
	print(array)
else:
	print("Specify the CEML script name")

