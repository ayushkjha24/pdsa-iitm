
from operator import itemgetter
 
def minimize_lateness(jobs):
    schedule =[]
    max_lateness = 0
    t = 0
     
    sorted_jobs = sorted(jobs,key=itemgetter(2))
     
    for job in sorted_jobs:
        job_start_time = t
        job_finish_time = t + job[1]
 
        t = job_finish_time
        if(job_finish_time > job[2]):
            max_lateness =  max (max_lateness, (job_finish_time - job[2]))
        schedule.append((job[0],job_start_time, job_finish_time))
 
    return max_lateness, schedule
 
jobs = [(1, 3, 6), (2, 2, 9), (3, 1, 8), (4, 4, 9), (5, 3, 14), (6, 2, 15)]
max_lateness, sc = minimize_lateness(jobs)
print ("Maximum lateness is :" + str(max_lateness))
for t in sc:
    print ('JobId= {0}, start time= {1}, finish time= {2}'.format(t[0],t[1],t[2]))