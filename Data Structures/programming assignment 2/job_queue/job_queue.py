# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        from heapq import heapify, heappop, heappush
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        scheduler = [(0, i) for i in range(self.num_workers)]
        heapify(scheduler)
        for i in range(len(self.jobs)):
            job_runtime = self.jobs[i]
            thread = heappop(scheduler)
            self.assigned_workers[i] = thread[1]
            self.start_times[i] = thread[0]
            heappush(scheduler, (thread[0] + job_runtime, thread[1]))
        
    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

