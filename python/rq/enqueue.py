
from rq import Queue, Worker
from redis import Redis
import time

# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue('calc_queue', connection=redis_conn)  # no args implies the default queue

q.empty()   # clean queue

from calc import square



job = q.enqueue(square, 5)
job = q.enqueue(square, 10)

print(job)

# print(job.result)

# time.sleep(2)

# print(job.result)
