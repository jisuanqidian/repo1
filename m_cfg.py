import sys
sys.path.append('/home/qiaochuli/bin/xsim')
from cfg import *

caseName.append('adder_sanity_test')

for i in range(1,101):
    caseName.append('addr_test_{:04d}'.format(i))

if __name__ == '__main__' :
    print(caseName)
