import sys
import os
import threading

# find -name 'pdb*.vdb' | xargs python3 single_merge.py

rootpath = os.getcwd()
threads = []
casenames = []

casenames = sys.argv[1:]

def run(cmd) :
    print('bsub -I ' + cmd)
    os.system('bsub -I ' + cmd)

for case in casenames:
    m_cmd = f'urg -full64 -dir {case} simv.vdb -report report/{case} -format text'
    thread = threading.Thread(target=run,args=(m_cmd,))
    thread.start()
    threads.append(thread)

for i in threads:
    i.join()
