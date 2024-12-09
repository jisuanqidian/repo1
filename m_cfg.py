import sys
sys.path.append('/home/qiaochuli/bin/xsim')
from cfg import *

com_opts['base'] = ''
com_opts['base'] += ''

caseName.append('adder_sanity_test')

for i in range(1,101):
    cn = 'test_{02d}'.format(i)
    depends[cn] = 'base'
    caseName.append(cn)
    if i == 1 : sim_opts[cn] = ' +UVM_TESTNAME= '

if __name__ == '__main__' :
    print(caseName)
