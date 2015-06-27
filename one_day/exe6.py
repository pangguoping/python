#!/usr/bin/env python
#_*_ coding:utf-8 _*_

info = 'This var will be printed out...'
name = raw_input('Please input your name:')
job = raw_input('Job：')
salary = raw_input('Salary:')

real_age = 29

for i in range(10):
  age = input('age:')
  if age > 29:
    print 'think smaller!'
  elif age == 29:
    print '\033[32;1mGOOD! 10 RMB!\033[0m'
  
    break
  else :
    print 'think bigger'
  print 'you still got %s shots!' % (9 - i)
print '''

Personal information of %s:
	 Name: %s
	 Age : %d
         Job : %s
        Salary: %s
------------------------
''' % (name,name,age,job,salary)
