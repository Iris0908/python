#python3
import sys
import time
class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__list = []

    def Search(self, a):
        left = 0
        right = len(self.__list)
        if right == 0:
            return 0
        while left != right:
            mid = int((left + right) / 2)
            if a < self.__list[mid][0]:
                right = mid
            elif a > self.__list[mid][0]:
                left = mid + 1
            else:
                return mid
        return left


    def Push(self, a):
        self.__stack.append(a)
        node = self.Search(a)
        if node == len(self.__list):
            self.__list.append([a, 1])
            return

        if a == self.__list[node][0]:
            self.__list[node][1] = self.__list[node][1] + 1
            return

        self.__list.insert(node, [a, 1])
        return


    def Pop(self):
        assert(len(self.__stack))
        stack_value = self.__stack.pop()
        node = self.Search(stack_value)

        if self.__list[node][1] > 1:
             self.__list[node][1] = self.__list[node][1] - 1
             return

        self.__list.pop(node)
        return
        

    def Max(self):
        assert(len(self.__stack))
        return self.__list[-1][0]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    #query = ["push", -1] 
    #num_queries = 400000
    #print(str(time.time()))
    for _ in range(num_queries):
        query = sys.stdin.readline().split()
        #if _ % 2 == 0:
        #    query[0] = "push"
        #    query[1] = query[1] + 1
        #else:
        #    query[0] = "max"

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
            #stack.Max()
        else:
            assert(0)

    #print(str(time.time()))
