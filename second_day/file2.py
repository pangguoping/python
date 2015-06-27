#!/usr/bin/env python

f = file('passwd.txt')

for i in f.readlines():
    i = i.strip('\n').split(':')
    
    print i

