#!/bin/usr/env python
name = ['a','b','2','c','d','2','e','f','2',]
first_pos = 0
for i in range(name.count('2')):
  new_list = name[first_pos:]
  next_pos = new_list.index('2') + 1
  print 'Find postion:',first_pos + new_list.index('2')
  first_pos += next_pos
