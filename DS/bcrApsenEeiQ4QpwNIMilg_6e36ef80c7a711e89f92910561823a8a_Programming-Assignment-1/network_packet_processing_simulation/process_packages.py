# python3

from collections import namedtuple
import queue
import time
import collections
import numpy as np

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, requests, reponses):
        head = 0
        last = 0
        index = 0
        current_time = 0
        runtime = 0
        req_len = len(requests)

        record_run = 0
        record_process = 0
        record_add = 0
        record_que = 0
        record_break = 0
        record_runtime = 0

        while index < req_len or head != last:
            record_run = record_run + 1
            #print(index, current_time, runtime, last-head)
            if runtime == 0:
                if head != last:
                    head = head + 1

                if head == last:#queue is empty, add package to queue and process it
                    if index < req_len: 
                        if current_time == requests[index].arrived_at:
                            self.finish_time.append(index)
                            last = last + 1
                            #print('add to queue---', index)
                            index = index + 1

                if head != last:    
                    reponses[self.finish_time[head]] = Response(False, current_time)
                    runtime = requests[self.finish_time[head]].time_to_process
                    record_process = record_process + 1
                    #if runtime == 0:
                    #    record_runtime = record_runtime+1
                    #    continue
                    #print('process from queue---', head, runtime, current_time)

            current_time = current_time + runtime
            if index < req_len:
                if current_time < requests[index].arrived_at:
                    current_time = current_time - runtime + 1
                    if runtime > 0:
                        runtime = runtime - 1
                    #print(runtime, current_time, index)
                    continue

            runtime = 0
            #2.add current time arrived packages to queue.
            while index < req_len:
                record_add = record_add+1 
                #print('add to queue---', index, current_time, requests[self.finish_time[head]].time_to_process, requests[index].arrived_at)
                #if current_time == requests[index].arrived_at:
                #if current_time < requests[index].arrived_at:
                #    current_time = current_time + 1
                 #   break
                if current_time > requests[index].arrived_at:
                    if last - head < self.size:
                        self.finish_time.append(index)
                        last = last + 1
                        record_que = record_que+1
                        #print('add to queue---', index)
                    index = index + 1
                else:
                    record_break = record_break+1
                    break

            #if runtime > 0:
            #    runtime = runtime - 1
            #current_time = current_time + 1
            #print('2---', index, current_time, runtime, head, last)
        #print(record_run, record_process, record_add, record_que, record_break, record_runtime, index)

def process_requests(requests, buffer):
    responses = []
    for req in requests:
        responses.append(Response(True, -1))
    buffer.process(requests, responses)
    return responses


def main():
    '''
    fl = str(input())
    fh = open('DS/bcrApsenEeiQ4QpwNIMilg_6e36ef80c7a711e89f92910561823a8a_Programming-Assignment-1/network_packet_processing_simulation/tests/'+fl, 'r')
    index = 0
    requests = []
    n_requests = 0
    for line in fh.readlines():
        if index == 0:
            buffer_size, n_requests = map(int, line.split())
            #print('size', buffer_size, 'number', n_requests)
        else:
            arrived_at, time_to_process = map(int, line.split())
            #print('arrived_at', arrived_at, 'time_to_process', time_to_process)
            requests.append(Request(arrived_at, time_to_process))
        index = index + 1
    '''

    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))
    
    #print(str(time.time()))

    buffer = Buffer(buffer_size)
    buffer.number = n_requests
    responses = process_requests(requests, buffer)

    #print(str(time.time()))
    
    for response in responses:
        print(response.started_at if not response.was_dropped else -1)
    
    '''
    fh = open('DS/bcrApsenEeiQ4QpwNIMilg_6e36ef80c7a711e89f92910561823a8a_Programming-Assignment-1/network_packet_processing_simulation/tests/'+fl+'.a', 'r')
    index = 1
    for line in fh.readlines():
        if int(line.strip('\n')) != int(responses[index-1].started_at):
            print('error', index, int(line.strip('\n')), int(responses[index-1].started_at))
            break
        index = index + 1
    '''

if __name__ == "__main__":
    main()
