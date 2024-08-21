import os
import re

def get_workpath() :
    workpath = os.getcwd()
    if os.path.isdir(workpath+'/env') != True and os.path.isdir(workpath+'/cfg') != True and os.path.isdir(workpath+'/th') != True:
        print('Warning: must work on module directory!')
        quit()
    else :
        workpath = workpath.split('/sim')[0]
        os.environ['WORKPATH'] = workpath
    return workpath

def check_keyword_in_file(filename,keywords=['Error','UVM_ERROR','UVM_FATAL'],skip_lines_num=10) :
    try :
        with open(filename, mode = 'r') as file :
            for skip in range(skip_lines_num) :
                next(file)
            for line in file :
                if 'UVM Report Summary' in line :
                    return 0
                if any(re.search(text,line,re.IGNORECASE) for text in keywords) :
                    return 1
        return 0
    except Exception as e :
        print(e)

if __name__ == '__main__' :
    print(check_keyword_in_file('test.txt',['^error']))
    print(check_keyword_in_file('test.txt'))
