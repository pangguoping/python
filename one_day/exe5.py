#!/usr/bin/env python
#_*_ coding:utf-8 _*_

name = raw_input('Please input your name:')

#age = raw_input('age:')
age = input('age:')

job = raw_input('Job:')

salary = raw_input('salary :')

if age > 40:
   msg = 'You are too old'
elif age > 30:
   msg = 'You are xx'
#else :
#   msg = 'You so young'

print '''
Personal information of %s:
	  Name: %s
          Age : %d
          Job : %s
       Salary : %s
--------------------------
%s
''' % (name,name,age,job,salary,msg)

