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
        #self.time = 0
        self.maxtime = 0
        self.number = 0

    def process(self, mlist, requests, reponses):
        #1.add input node to buff.
        for arrave_time in sorted(mlist):
            while len(mlist[arrave_time]) != 0:
                #print('self.size', self.size, len(self.finish_time), 'arrave_time', arrave_time)
                if len(self.finish_time) < self.size:
                    #print('1 insert to self.finish_time', mlist[arrave_time][-1])
                    #self.finish_time.insert(0, mlist[arrave_time].pop())
                    self.finish_time.append(mlist[arrave_time].pop())
                    #self.time = self.time + requests[self.finish_time[-1]].time_to_process
                else:
                    break
            if len(self.finish_time) == self.size:
                break

        #self.finish_time.reverse()
        #print('4', str(time.time()))
        #2.pick up one node from buff and add rest one to buff, then process
        current_time = 0
        flag = 0
        run_time = 0
        #number = 0
        #while len(self.finish_time) != flag:
        while(current_time < self.maxtime or len(self.finish_time) > flag):
            #print('number', self.number, number)
            #if self.number == number+1:
            #    break
            arrave_time = current_time

            if len(self.finish_time) - flag < self.size  and arrave_time in mlist:
                print('8', arrave_time, len(mlist[arrave_time]))
                if len(mlist[arrave_time]) != 0:
                    self.finish_time.append(mlist[arrave_time].pop())
                    #self.time = self.time + requests[self.finish_time[-1]].time_to_process
                    print('arrave_time', arrave_time, self.finish_time[-1])

            if len(self.finish_time) > flag:
                #number = number + 1
                index = self.finish_time[flag]
                #print('3 process index', index)
                if current_time < requests[index].arrived_at:
                    current_time = current_time + 1
                    #run_time = run_time + 1
                #    current_time = requests[index].arrived_at
                    continue
                if run_time < requests[index].time_to_process:
                    run_time = run_time + 1
                    current_time = current_time + 1
                    continue
                reponses[index] = Response(False, current_time)
                print('5 process index', index, current_time, flag, len(self.finish_time))
                #current_time = current_time + requests[index].time_to_process
                #self.finish_time.pop(0)
                flag = flag + 1
                run_time = 0
                #current_time = current_time + requests[index].time_to_process
            #else:
            current_time = current_time + 1
            #run_time = run_time - 1
            #arrave_time = current_time
            #while(arrave_time <= self.maxtime):
            #if arrave_time in mlist:
            #    print('8', arrave_time, len(mlist[arrave_time]))
            #    if len(mlist[arrave_time]) != 0:
            #        self.finish_time.append(mlist[arrave_time].pop())
                    #self.time = self.time + requests[self.finish_time[-1]].time_to_process
            #        print('arrave_time', arrave_time, self.finish_time[-1])
                    #break
                #arrave_time = arrave_time + 1       
            #current_time = current_time + requests[index].time_to_process
            #ret = False
            #for arrave_time in sorted(mlist):
            #    if ret == True:
            #        break
                #if arrave_time < current_time + self.time:
                    #continue
                #while len(mlist[arrave_time]) != 0:
                    #if len(self.finish_time) < self.size:
                        #print('2 insert to self.finish_time', mlist[arrave_time][-1])
                    #self.finish_time.append(mlist[arrave_time].pop())
                    #self.time = self.time + requests[self.finish_time[-1]].time_to_process
                    #ret = True
                    #break
                    #else:
                    #    break
                #if len(self.finish_time) == self.size:
                #    break
            

def process_requests(requests, buffer):
    responses = []
    mlist = {}
    index = 0
    for request in requests:
        buffer.maxtime = max(buffer.maxtime, request.arrived_at)
        responses.append(Response(True, -1))
        if request.arrived_at in mlist:
            mlist[request.arrived_at].append(index)
        else:
            mlist[request.arrived_at] = [index]
        index = index + 1

    print('2', str(time.time()))

    for arrave_time in mlist:
        mlist[arrave_time].reverse()

    print('3', str(time.time()))

    buffer.process(mlist, requests, responses)

    return responses


def main():
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


    #buffer_size, n_requests = map(int, input().split())
    #requests = []
    #for _ in range(n_requests):
    #    arrived_at, time_to_process = map(int, input().split())
    #    requests.append(Request(arrived_at, time_to_process))

    print('1', str(time.time()))

    buffer = Buffer(buffer_size)
    buffer.number = n_requests
    responses = process_requests(requests, buffer)

    print(str(time.time()))

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)
    
    fh = open('DS/bcrApsenEeiQ4QpwNIMilg_6e36ef80c7a711e89f92910561823a8a_Programming-Assignment-1/network_packet_processing_simulation/tests/'+fl+'.a', 'r')
    index = 1
    for line in fh.readlines():
        if int(line.strip('\n')) != int(responses[index-1].started_at):
            print('error', index, int(line.strip('\n')), int(responses[index-1].started_at), buffer.maxtime)
            break
        index = index + 1
       

if __name__ == "__main__":
    main()
