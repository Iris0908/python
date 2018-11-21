# python3

from collections import namedtuple
import queue
import time

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, mlist, requests, reponses):
        #1.add input node to buff.
        for arrave_time in sorted(mlist):
            while len(mlist[arrave_time]) != 0:
                if len(self.finish_time) < self.size:
                    #print('1 insert to self.finish_time', mlist[arrave_time][-1])
                    self.finish_time.insert(0, mlist[arrave_time].pop())
                else:
                    break
            if len(self.finish_time) == self.size:
                break

        #2.pick up one node from buff and add rest one to buff, then process
        current_time = 0
        while len(self.finish_time) != 0:
            index = self.finish_time[-1]
            #print('3 process index', index)
            if current_time < requests[index].arrived_at:
                current_time = current_time + 1
                continue
            reponses[index] = Response(False, current_time)
            #print('4 process index', index)
            current_time = current_time + requests[index].time_to_process
            self.finish_time.pop()

            for arrave_time in sorted(mlist):
                if arrave_time < current_time:
                    continue
                while len(mlist[arrave_time]) != 0:
                    if len(self.finish_time) < self.size:
                        #print('2 insert to self.finish_time', mlist[arrave_time][-1])
                        self.finish_time.insert(0, mlist[arrave_time].pop())
                    else:
                        break
                if len(self.finish_time) == self.size:
                    break


def process_requests(requests, buffer):
    responses = []
    mlist = {}
    index = 0
    for request in requests:
        responses.append(Response(True, -1))
        if request.arrived_at in mlist:
            mlist[request.arrived_at].append(index)
        else:
            mlist[request.arrived_at] = [index]
        index = index + 1

    for arrave_time in mlist:
        mlist[arrave_time].reverse()

    buffer.process(mlist, requests, responses)

    return responses


def main():
    fh = open('D:\\work\\python\\git\\python-project\\DS\\bcrApsenEeiQ4QpwNIMilg_6e36ef80c7a711e89f92910561823a8a_Programming-Assignment-1\\network_packet_processing_simulation\\tests\\22', 'r')
    index = 0
    requests = []
    for line in fh.readlines():
        if index == 0:
            buffer_size, n_requests = map(int, line.split())
            #print('size', buffer_size, 'number', n_requests)
        else:
            arrived_at, time_to_process = map(int, line.split())
            #print('arrived_at', arrived_at, 'time_to_process', time_to_process)
            requests.append(Request(arrived_at, time_to_process))
        index = index + 1


    #buffer_size, n_requests = map(int, input().split())
    #requests = []
    #for _ in range(n_requests):
    #    arrived_at, time_to_process = map(int, input().split())
    #    requests.append(Request(arrived_at, time_to_process))

    start = time.time()
    print(str(start))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    end = time.time()
    print(str(end))

    #for response in responses:
    #    print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
