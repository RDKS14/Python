#!/usr/bin/python

# Example Python script
import sys

argc = len(sys.argv)

if argc >1:
print ('too many args')
else: where = 'World'

print("hello", where)

print('goodbye from' + sys.argv[0])