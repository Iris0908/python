# python3
import time

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

        '''
        fh = open('DS/_239b6711c9a70f442e40e1a1c2261912_Programming-Assignment-2/job_queue/tests/08', 'r')
        index = 0
        for line in fh.readlines():
            if index == 0:
                self.num_workers, m = map(int, line.split())
                index = index + 1
                #print('size', buffer_size, 'number', n_requests)
            else:
                self.jobs = list(map(int, line.split()))
        '''

    def write_response(self):
        '''
        fh = open('DS/_239b6711c9a70f442e40e1a1c2261912_Programming-Assignment-2/job_queue/tests/08.a', 'r')
        index = 0
        for line in fh.readlines():
            swap_test_0, swap_test_1 = map(int, line.split())
            if swap_test_0 != self.assigned_workers[index] or swap_test_1 != self.start_times[index]:
                print('error', index+1, swap_test_0, swap_test_1, self.assigned_workers[index], self.start_times[index])
                break
            index = index + 1
        '''
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        #next_free_time = [[0]] * self.num_workers
        next_free_time = []
        for i in range(self.num_workers):
            next_free_time.append([i, 0])
        
        root = 0
        for i in range(len(self.jobs)):
            next_worker = root
            self.assigned_workers[i] = next_free_time[next_worker][0]
            self.start_times[i] = next_free_time[next_worker][1]
            next_free_time[next_worker][1] += self.jobs[i]

            #shift-down min-heap
            min = root
            node = root
            while 2*node + 1 < self.num_workers:
                if next_free_time[min][1] == next_free_time[2*node + 1][1]:
                    if next_free_time[min][0] > next_free_time[2*node + 1][0]:
                        min = 2*node + 1

                #print('0000000:', node, min, self._data[min], self._data[2*node + 1])
                if next_free_time[min][1] > next_free_time[2*node + 1][1]:
                    min = 2*node + 1
                    #print('qqqq:', node, 2*node + 1)
        
                if 2*node + 2 >= self.num_workers:
                    if min != node:
                        #self._swaps.append((node, min))
                        #print('wwww, swap:', node, min, self._data[node], self._data[min])
                        next_free_time[min], next_free_time[node] = next_free_time[node], next_free_time[min]
                    break

                if next_free_time[min][1] == next_free_time[2*node + 2][1]:
                    if next_free_time[min][0] > next_free_time[2*node + 2][0]:
                        min = 2*node + 2

                if next_free_time[min][1] > next_free_time[2*node + 2][1]:
                    min = 2*node + 2
                    #print('eeee:', 2*node + 2)

                if min != node:
                    #self._swaps.append((node, min))
                    #print('rrrr, swap:', node, min, self._data[node], self._data[min])          
                    next_free_time[min], next_free_time[node] = next_free_time[node], next_free_time[min]
                    node = min
                else:
                    #print('tttt:', node, min, self._data[node], self._data[2*node + 1], self._data[2*node + 2])
                    break

    def solve(self):
        self.read_data()
        #print(str(time.time()))
        self.assign_jobs()
        #print(str(time.time()))
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

