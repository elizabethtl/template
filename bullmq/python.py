import asyncio

from bullmq import Queue
from bullmq import Worker

async def process(job, job_token):
    # job.data will include the data added to the queue
    print(f"job name: {job}, token: {job_token}")
    print(job.data)
    print(job.data['foo'])
    print(job.name)

async def main():

  queue = Queue('myQueue')
  await queue.add('myjob1', {'foo': 'bar1'})
  await queue.add('myjob2', {'foo': 'bar2'})
  await queue.add('myjob3', {'foo': 'bar3'})

  # Feel free to remove the connection parameter, if your redis runs on localhost
  worker1 = Worker("myQueue", process)
  worker2 = Worker("myQueue", process)

  # This while loop is just for the sake of this example
  # you won't need it in practice.
  while True: # Add some breaking conditions here
    await asyncio.sleep(0.1)
    break

  # When no need to process more jobs we should close the worker
  await worker1.close()
  await worker2.close()

  await queue.close()


if __name__ == "__main__":
    asyncio.run(main())
