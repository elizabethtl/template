# https://gist.github.com/prempv/717270a4470a10146c6776820e8e3cbc

from multiprocessing import Process, Queue
from time import sleep
from random import random

class Worker(Process):
    def __init__(self, input_queue, output_queue):
        Process.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue

    def run(self):
        while True:
            if self.input_queue.empty() == True:
                break
            else:
                item = self.input_queue.get()
                sleep(random())
                self.output_queue.put(item*10)
                # print(f"Processed {item}")
        return


def dispatchWorker():
    task_q = Queue(maxsize=50)
    output_q = Queue()

    results_bank = []

    for i in range(20):
        task_q.put(i)

    processes = [
        Worker(task_q, output_q)
        for i in range(5)
    ]

    for proc in processes:
        proc.start()

    remaining = set(range(20, 100))
    results_bank = []

    while True:
        if remaining:
            task_q.put(remaining.pop())
            if output_q.empty() != True:
                results_bank.append(output_q.get_nowait())
        else:
            break

    for proc in processes:
        proc.join()

    print("Join complete")
    
    while output_q.empty() != True:
        results_bank.append(output_q.get_nowait())


    # length of this list should be equal to static_input, which is the range used to populate the input queue. In other words, this tells whether all the items placed for processing were actually processed.
    print("Results: ", len(results_bank))
    print("Remaining: ", len(remaining))


if __name__ == '__main__':
    dispatchWorker()
