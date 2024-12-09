import os
import re
import sys

def get_workpath() :
    workpath = os.getcwd()
    if os.path.isdir(workpath+'/env') != True and os.path.isdir(workpath+'/cfg') != True and os.path.isdir(workpath+'/th') != True:
        print('Warning: must work on module directory!')
        sys.exit()
    else :
        workpath = workpath.split('/sim')[0]
        os.environ['WORKPATH'] = workpath
    return workpath

def check_keyword_in_file(filename,keywords=[r'^\bError\b','UVM_ERROR','UVM_FATAL','offending'],skip_lines_num=10) :
    try :
        with open(filename, mode = 'r') as file :
            for skip in range(skip_lines_num) :
                next(file)
            for line in file :
                if re.search('UVM Report.*Summary',line) != None :
                    return 0
                if any(re.search(text,line,re.IGNORECASE) for text in keywords) :
                    return 1
        return 0
    except Exception as e :
        print(e)
        return 1

def rename_hist_files(path, file_name):
    if not os.path.exists(path):
        print("The specified path does not exist.")
        return
    pattern = re.compile(r'^' + re.escape(file_name) + r'\.(\d+)$')
    file_ind_list = [int(i.split('.')[-1]) for i in os.listdir(path) if pattern.match(i) != None]
    file_ind_list.sort(reverse=True)
    ori_file = os.path.join(path, f'{file_name}')
    for ind,i in zip(range(len(file_ind_list)-1,0-1,-1),file_ind_list):
        if(ind == i and os.path.exists(ori_file)):
            old_file = os.path.join(path, f'{file_name}.{i}')
            new_file = os.path.join(path, f'{file_name}.{i+1}')
            os.rename(old_file,new_file)
    if(os.path.exists(ori_file)):
        new_file = os.path.join(path, f'{file_name}.0')
        os.rename(ori_file,new_file)

if __name__ == '__main__' :
    print(check_keyword_in_file('test.txt',['^error']))
    print(check_keyword_in_file('test.txt'))
