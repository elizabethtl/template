from rq import Queue, Worker
from redis import Redis
# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue('calc_queue', connection=redis_conn)

w = Worker([q], connection=redis_conn)
w.work()

# need separate scripts for separate workers
