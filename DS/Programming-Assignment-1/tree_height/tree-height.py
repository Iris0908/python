# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                chiled = {}                      
                for vertex in range(self.n):
                        if self.parent[vertex] == -1:
                                self.root = vertex
                        else:
                                if self.parent[vertex] in chiled:
                                        chiled[self.parent[vertex]].append(vertex)
                                else:
                                        chiled[self.parent[vertex]] = [vertex]


                list1 = []
                list2 = []
                self.height = 0
                if len(chiled) != 0:
                        list1.append(chiled[self.root])
                while (True):
                        if len(list1) == 0 and len(list2) == 0:
                                break;
                        if len(list1) != 0:
                                for node in list1:
                                        for ch in node:
                                                if ch in chiled:
                                                        list2.append(chiled[ch])
                                list1.clear()
                                self.height = self.height + 1

                        if len(list2) != 0:
                                for node in list2:
                                        for ch in node:
                                                if ch in chiled:
                                                        list1.append(chiled[ch])
                                list2.clear()
                                self.height = self.height + 1
                         
                return self.height+1



def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
