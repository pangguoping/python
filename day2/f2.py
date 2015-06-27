import time
import fileinput
for line in fileinput.input('f_test.txt',inplace=0):
	line = line.replace("the 4 loops","change me 4")
	print line,
