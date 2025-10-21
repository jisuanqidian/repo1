import sys
sys.path.append('/home/qiaochuli/bin/xsim')
from cfg import *

com_opts['base']  = ''

for i,ind in zip(['base'],range(1,1+1)):
    cn = 'rtl_{:s}_{:04d}'.format(i,ind)
    depends[cn] = 'base'
    caseName.append(cn)
    sim_opts[cn] = f' +UVM_TESTNAME=test0'
    if ind == 1 : sim_opts[cn] += ''

com_opts['i2c']  = ' +define+ENABLE_I2C'
com_opts['i2c'] += ' +define+SVT_I2C_NUM_MASTER=2'
com_opts['i2c'] += ' +define+SVT_I2C_NUM_SLAVE=2'
com_opts['i2c'] += ' +define+UVM_PACKER_MAX_BYTES=150000'
com_opts['i2c'] += ' -f ../cfg/svt.f'

for i,ind in zip(['i2c'],range(1,1+1)):
    cn = 'rtl_{:s}_{:04d}'.format(i,ind)
    depends[cn] = 'i2c'
    caseName.append(cn)
    sim_opts[cn] = f' +UVM_TESTNAME=test0'
    if ind == 1 : sim_opts[cn] += ' +sequence=i2c_sequence'

if __name__ == '__main__' :
    for i in caseName:
        print(i)
        try:
            print(sim_opts[i])
        except:
            pass
