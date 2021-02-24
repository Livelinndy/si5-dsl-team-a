#!/usr/bin/python
import re
import sys
#from pyCinEditorML.src.AppBuilder import AppBuilder

"""
DSL version of the demo application
Usage example: Main.py test1
Where "test1" is the name of a .ceml script from the resources folder
"""

# pas encore lie avec AppBuilder

if len(sys.argv) > 1:
	file = open('../resources/scenarios/' + sys.argv[1] + '.ceml')
	text = file.read()
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
	file.close()
    print(finalArray)
else:
	print("Specify the CEML script name")

