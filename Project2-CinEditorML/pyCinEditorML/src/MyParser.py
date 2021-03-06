import sys
sys.path.append('../')

from kernel.AppInit import AppInit
from kernel.Clips import Video, Blank
from kernel.Actions import Action, AddText, \
	Concatenate, ConcatenateWithTransition, Superpose, Export
from Exceptions import UndefinedAction, UndefinedClip, SyntaxError

def parseVideo(variableName, line):
	s = line.split('"')
	filename = s[1]
	if s[2] != '':
		s1 = s.split(' ')
		if s[0] == 'from' and s[2] == 'to':
			from_time = s[1]
			to_time = s[3]
			return Video(variableName, filename, from_time, to_time)
		else:
			raise SyntaxError()
	return Video(variableName, filename)

def parseBlank(variableName, line):
	s = line.split(' ')
	if s[2] == 'color':
		color = s[3]
		if s[4] == 'background' and s[5] == 'during':
			duration = s[6]
			return Blank(variableName, duration, color)
	raise SyntaxError()
	
def parseClip(line):
	s = line.split(' ')
	variableName = s[1]
	if s[2] == 'is':
		return parseVideo(variableName, line)
	else if s[2] == 'color':
		return parseBlank(variableName, line)
	raise UndefinedClip()

	
def parseAddTitle(line):
	s = line.split('"')
	text = s[2]
	pass

def parseAddSubtitle(line):
	s = line.split('"')
	text = s[2]
	pass

def parseAddText(line):
	s = line.split('"')
	text = s[2]
	pass
	
def parseSuperpose(line):
	s = line.split(' ')
	side_clip = s[2]
	pos_x = s[5]
	pos_y = s[4]
	ratio = s[7]
	main_clip = s[9]
	return Superpose(main_clip, side_clip, pos_x, pos_y, ratio)
	
def parseAdd(line):
	s = line.split(' ')
	if s[1] == 'title':
		return parseAddTitle(line)
	else if s[1] == 'subtitle':
		return parseAddSubtitle(line)
	else if s[1] == 'text':
		return parseAddText(line)
	else if s[1] == 'clip':
		return action = parseSuperpose(line)
	raise UndefinedAction()

def parseConcat(line):
	s = line.split(' ')
	clips = [s[1]]
	i = 2
	while s[i] == 'and':
		clips.append(s[i+1])
		i += 2
	if s[i] == 'to':
		dest = s[i+1]
		return Concatenate(clips, dest)
	else if s[i] == 'with' and s[i+1] == 'transition':
		i += 2
		transition = s[i]
		if s[i+1] == 'to':
			dest = s[i+2]
			return ConcatenateWithTransition(clips, dest, transition)
	raise SyntaxError()

def parseExport(line):
	s = line.split(' ')
	dest = s[1]
	if s[2] != 'as':
		raise SyntaxError()
	s = line.split('"')
	filename = s[1]
	return Export(dest, filename)
		
def getSequenceOfActions(lines):
	actions = [AppInit()]
	for line in lines:
		action = None
		s = line.split(' ')
		if s[0] == 'clip':
			action = parseClip(line)
		else if s[0] == 'add':
			action = parseAdd(line)
		else if s[0] == 'concat':
			action = parseConcat(line)
		else if s[0] == 'export':
			action = parseExport(line)
		else:
			raise UndefinedAction()
		if action is not None:
			actions.append(action)
			
def translateCemlToPython(lines):
	actions = getSequenceOfActions(lines)
	code = ""
    for a in actions:
        code += a.execute()
    return code
