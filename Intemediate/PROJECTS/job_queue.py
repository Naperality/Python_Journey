# print_queue_simulator.py
from collections import deque

class PrintQueue:
    def __init__(self):
        self.queue = deque()

    def add_job(self, job_name):
        self.queue.append(job_name)
        print(f"Added job: {job_name}")

    def process_job(self):
        if self.queue:
            job = self.queue.popleft()
            print(f"Processing job: {job}")
        else:
            print("No jobs in queue.")

    def show_queue(self):
        print("Queue:", list(self.queue))

# Demo
pq = PrintQueue()
pq.add_job("Document1")
pq.add_job("Image2")
pq.show_queue()
pq.process_job()
pq.show_queue()
