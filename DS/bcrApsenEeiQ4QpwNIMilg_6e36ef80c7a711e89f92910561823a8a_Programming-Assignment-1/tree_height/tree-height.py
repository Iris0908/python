# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height_old(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height)
                return maxHeight


        def recurs(self, child):
                if child not in self.chiled:
                        return 1
                else:
                        h = self.recurs(vertex) + 1
                        self.height = max(self.height, h)
                        return h


        def compute_height(self):
                self.height = 0
                self.chiled = {}             
                for vertex in range(self.n):
                        if self.parent[vertex] == -1:
                                self.root = vertex
                        else:
                                if self.parent[vertex] in self.chiled:
                                        self.chiled[self.parent[vertex]].append(vertex)
                                else:
                                        self.chiled[self.parent[vertex]] = [vertex]

                child = self.root
                for vertex in self.chiled[child]:
                        self.recurs(self.root)

                return self.height
'''

                if len(chiled) != 0:
                        self.height = 1
                        stack.append(chiled[self.root])

                while len(stack) != 0:
                        flag = False
                        index = 0
                        if stack[-1][0] != -1:
                                self.height = self.height + 1
                        for ch in stack[-1]:
                                print(ch)
                                print('height: ', self.height)
                                if ch != -1:
                                        if ch in chiled:
                                                stack.append(chiled[ch])
                                                stack[-2][index] = -1
                                        else:
                                                stack[-1][index] = -1

                                        flag = True
                                        break
                                index = index + 1
                                #if index == 10:
                        #return
                        if flag == False:
                                #return
                                stack.pop()
'''



def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
