#_*_coding:utf-8
import sys,os
if line(sys,argv) <=1:
   print "USAGE:./file_replace.py old_text new_text filename"
old_text,new_text = sys.argv[1],sys.argv[2]

file_name = sys_argv[3]

f = file(file_name,'rb')
for line in f.xreadlines():
    print line.replace(old_text,new_text)
replace_file
