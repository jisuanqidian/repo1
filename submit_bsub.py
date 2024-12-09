import subprocess
import threading
import time
import sys
from info import *

job_num = 0

def submit_job(command,job_info) :
    #print(f'submitting {command}')
    output = subprocess.check_output('bsub '+command, shell=True).decode()
    job_id = None

    for line in output.splitlines() :
        if 'is submitted to default queue' in line :
            job_id = line.split()[1].strip('<>')
            break

    if job_id is None :
        raise RuntimeError(f'Failed to submit job: {command}')

    print(green_info(f'[{job_info}]')+f' Job submitted with ID: {job_id}')
    return job_id

def check_job_status(job_id) :
    command = f'bjobs {job_id}'
    output = subprocess.check_output(command, shell=True).decode()

    status = None
    for line in output.splitlines() :
        if job_id in line :
            status = line.split()[2]
            break

    return status

def monitor_job(job_id,job_info) :
    global job_num
    start_time = time.time()
    while True :
        status = check_job_status(job_id)
        if status in ['DONE', 'EXIT'] :
            end_time = time.time()
            elaspsed_time = end_time - start_time
            time_d = time_transform(elaspsed_time)
            print(green_info(f'[{job_info}]')+f' Job {job_id} has completed with status: {status} in' + print_time(time_d))
            job_num -= 1
            break
        else :
            end_time = time.time()
            elaspsed_time = end_time - start_time
            time_d = time_transform(elaspsed_time)
            print_info = green_info(f'[{job_info}]')+f' Job {job_id} is running with status: {status} for' + print_time(time_d)
            sys.stdout.write(f'\r{print_info}\n')
            sys.stdout.flush()
            #print(green_info(f'[{job_info}]')+f' Job {job_id} is running with status: {status} for' + print_time(time_d))
            time.sleep(2.5)

def summary_info() :
    global job_num
    start_time = time.time()
    while job_num != 0 :
        current_time = time.time()
        elaspsed_time = current_time - start_time
        time_d = time_transform(elaspsed_time)
        #print('\rregression has running for' + print_time(time_d))
        sys.stdout.write('\rregression has running for' + print_time(time_d) + '\n')
        sys.stdout.flush()
        time.sleep(1)

def time_transform(seconds) :
    time_d = {}
    time_d['hour'],remainder = divmod(int(seconds),3600)
    time_d['minute'],time_d['second'] = divmod(remainder,60)
    return time_d

def print_time(time_d) :
    hour = f' {time_d["hour"]} hours' if time_d["hour"] > 0 else ''
    minute = f' {time_d["minute"]} minutes' if not (time_d["hour"] == 0 and time_d["minute"] == 0) else ''
    second = f' {time_d["second"]} seconds'
    return hour + minute + second

def main(job_commands,job_infos) :
    global job_num

    job_ids = []

    if isinstance(job_commands,list):
        for command,job_info in zip(job_commands,job_infos) :
            job_id = submit_job(command,job_info)
            job_ids.append(job_id)
    else :
        job_id = submit_job(job_commands,job_infos)
        job_ids.append(job_id)
        job_infos = [job_infos]

    threads = []

    for job_id,job_info in zip(job_ids,job_infos) :
        thread = threading.Thread(target=monitor_job, args=(job_id,job_info,))
        thread.start()
        threads.append(thread)
        job_num += 1

#    thread = threading.Thread(target=summary_info)
#    thread.start()
#    threads.append(thread)

    for thread in threads :
        thread.join()

    print('All jobs have completed.')

if __name__ == '__main__' :
    job_commands = [
        'bsub sleep 2',
        'bsub sleep 2',
        'bsub sleep 2',
    ]
    job_infos = ['sleep2','sleep2','sleep2']
    main(job_commands,job_infos)
