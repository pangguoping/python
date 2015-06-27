import time
import fileinput

for line in fileinput.input('f_test.txt',inplace=1):
	line = line.replace("the 26 loops\n","change me\n")
	print line,



"""
f = file("f_test.txt",'r')
file_content = f.readlines()
print file_content
"""
"""
for i in range(15,31):
        time.sleep(1)
	f.write('the %s loops\n' % i)
	f.flush()
time.sleep(10)
f.close()
"""
