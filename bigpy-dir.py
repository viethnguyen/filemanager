'''
Copyright Mark Lutz - Programming Python
Find the largest Python source file in a single directory
Search WIndows Python source lib, unless dir command-line arg.
'''

import os, glob, sys
dirname = r'~/@code/Python' if len(sys.argv) == 1 else sys.argv[1]

allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
	filesize = os.path.getsize(filename)
	allsizes.append((filesize, filename))
	
allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])
