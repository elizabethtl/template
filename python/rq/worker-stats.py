# from rq.registry import StartedJobRegistry, FinishedJobRegistry, FailedJobRegistry

from rq import Queue, Worker
from redis import Redis
# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue('calc_queue', connection=redis_conn)

print(len(q))
print(q)

print(q.get_job_ids())

workers = Worker.all(queue=q)
print(workers)

w1 = workers[0]
# w2 = workers[1]

print(f'Successful jobs: {w1.successful_job_count}')
print(f'Failed jobs: {w1.failed_job_count}')
print(f'Total working time: {w1.total_working_time}')

