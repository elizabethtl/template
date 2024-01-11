# from rq.registry import StartedJobRegistry, FinishedJobRegistry, FailedJobRegistry

from rq import Queue, Worker
from redis import Redis
# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue('calc_queue', connection=redis_conn)

print(len(q))
print(q)

# print(q.get_job_ids())

print(q.scheduled_job_registry.count)
print(q.deferred_job_registry.count)
print(q.started_job_registry.count)
print(q.finished_job_registry.count)
print(q.failed_job_registry.count)
