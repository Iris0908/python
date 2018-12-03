# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    #n = int(input())
    #self._data = [int(s) for s in input().split()]
    
    fh = open('DS/_239b6711c9a70f442e40e1a1c2261912_Programming-Assignment-2/make_heap/tests/04', 'r')
    index = 0
    for line in fh.readlines():
        if index == 0:
            #n = int(line.split())
            index = index + 1
            #print('size', buffer_size, 'number', n_requests)
        else:
            self._data = line.split()
    
    #assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    #for swap in self._swaps:
      #print(swap[0], swap[1])
    fh = open('DS/_239b6711c9a70f442e40e1a1c2261912_Programming-Assignment-2/make_heap/tests/04.a', 'r')
    index = 0
    for line in fh.readlines():
        if index == 0:
            #n = int(line.split())
            pass
        else:
            swap_0 = self._swaps[index-1][0]
            swap_1 = self._swaps[index-1][1]
            swap_test_0, swap_test_1 = map(int, line.split())
            if swap_test_0 != swap_0 or swap_test_1 != swap_1:
                print('error', index+1, swap_test_0, swap_test_1, swap_0, swap_1)
                break
        index = index + 1


  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    '''
    for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]
    '''

    lengh = len(self._data)
    for i in range(int(lengh/2) - 1, -1, -1):
      #print('rang:', i)
      min = i
      node = i
      while 2*node + 1 < lengh:
        if self._data[min] > self._data[2*node + 1]:
          min = 2*node + 1
          #print('qqqq:', node)
        
        if 2*node + 2 >= lengh:
          if min != node:
            self._swaps.append((node, min))
            self._data[min], self._data[node] = self._data[node], self._data[min]
            #print('wwww:', node)
          break

        if self._data[min] > self._data[2*node + 2]:
          min = 2*node + 2
          #print('eeee:', node)

        if min != node:
          self._swaps.append((node, min))
          self._data[min], self._data[node] = self._data[node], self._data[min]
          node = min
          #print('rrrr:', node)
        else:
          #print('tttt:', node)
          break

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
