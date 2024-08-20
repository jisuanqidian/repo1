#!/bin/python3.6

import os
import sys

file_name = sys.argv[1:]
cmdline = 'gvim -O'
first_file = None

for i in file_name:
    if ':' in i and not first_file:
        first_file = i
    cmdline += i.split(':')[0] + ' '

try :
    if first_file.split(':')[1].isdigit():
        cmdline += '+' + first_file.split(':')[1]
except Exception as e:
    pass

print(cmdline)
os.system(cmdline)
