'''
JS-Beautify
This is a tool to beautify all the JS files present in the directory
and subdirs. The tool used jsbeautifier lib for the process and below is its
reference link

https://github.com/beautify-web/js-beautify

Autor : Brijesh
Date : 26-01-2016
Github: 
'''

import os
import sys
import jsbeautifier
from fnmatch import fnmatch

def beautifyFiles (path, name) :
	fPath = os.path.join(path, name)
	res = jsbeautifier.beautify_file(fPath)
	output = open(fPath, "w+")
	output.write(res)
	output.close()
	print fPath

def searchFiles(root, pattern) :
	for path, subdirs, files in os.walk(root):
	    for name in files:
	        if fnmatch(name, pattern) :
	    		beautifyFiles(path, name)

def prepareFileSearch (sysArgs) : 
	argCount = len(sysArgs)
	root = sysArgs[0]
	pattern = "*.js"
	searchFiles(root, pattern)

def main (sysArgs) :
	if sysArgs == []:
		print "[ERROR] : Root directory must be passed as a parameter."
	else :
		prepareFileSearch(sysArgs)
		

main(sys.argv[1:])
