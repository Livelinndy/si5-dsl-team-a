#!/usr/bin/python

import sys
#from pyCinEditorML.src.AppBuilder import AppBuilder

"""
DSL version of the demo application
Usage example: Main.py test1
Where "test1" is the name of a .ceml script from the resources folder
"""

# pas encore lie avec AppBuilder

if len(sys.argv) > 1:
	file = open('../resources/scenarios/' + sys.argv[1] + '.ceml', 'r')
	lines = file.readlines()
 
	count = 0
	
	for line in lines:
		line = line.strip() # strips the newline character
		count += 1
		print("Line{}: {}".format(count, line))
	
	file.close()
else:
	print("Specify the CEML script name")

