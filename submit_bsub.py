import subprocess
import threading
import time
from info import *

def submit_job(command) :
    #print(f'submitting {command}')
    output = subprocess.check_output('bsub '+command, shell=True).decode()
    job_id = None

    for line in output.splitlines() :
        if 'is submitted to default queue' in line :
            job_id = line.split()[1].strip('<>')
            break

    if job_id is None :
        raise RuntimeError(f'Failed to submit job: {command}')

    print(f'Job submitted with ID: {job_id}')
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
    while True :
        status = check_job_status(job_id)
        if status in ['DONE', 'EXIT'] :
            print(green_info(f'[{job_info}]')+f' Job {job_id} has completed with status: {status}')
            break
        else :
            print(green_info(f'[{job_info}]')+f' Job {job_id} is running with status: {status}.')
            time.sleep(2.5)

def main(job_commands,job_infos) :

    job_ids = []

    if isinstance(job_commands,list):
        for command in job_commands :
            job_id = submit_job(command)
            job_ids.append(job_id)
    else :
        job_id = submit_job(job_commands)
        job_ids.append(job_id)
        job_infos = [job_infos]

    threads = []

    for job_id,job_info in zip(job_ids,job_infos) :
        thread = threading.Thread(target=monitor_job, args=(job_id,job_info,))
        thread.start()
        threads.append(thread)

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
