#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__tree = []
        self.root = -1
        self.h_left = 0
        self.h_right = 0

    def Balance(self, a):
        left_child = 0
        right_child = 0
        if a < self.__tree[self.root][0]:
            if self.h_left > self.h_right:
                left_child = self.__tree[self.root][1]
                node = self.__tree[left_child][2]
                self.__tree[left_child][2] = self.root
                self.__tree[self.root][1] = node
                self.root = left_child
        elif a > self.__tree[self.root][0]:
            if self.h_left < self.h_right:
                right_child = self.__tree[self.root][2]
                node = self.__tree[right_child][1]
                self.__tree[right_child][1] = self.root
                self.__tree[self.root][2] = node
                self.root = right_child

    def Push(self, a):
        if self.root == -1:
            self.root = 0
            self.__tree.append([a, -1, -1, 1])
        else:
            height = 0
            left_child = self.__tree[self.root][1]
            right_child = self.__tree[self.root][2]
            node_value = self.__tree[self.root][0]
            node = self.root
            while (True):
                if a < node_value:
                    if left_child == -1:
                        self.__tree.append([a, -1, -1, 1])
                        self.__tree[node][1] = len(self.__tree) - 1
                        if self.__tree[node][2] == -1:
                            height = height + 1
                            if a < self.__tree[self.root][0]:
                                if height > self.h_left:
                                    self.Balance(a)
                                self.h_left = max(self.h_left, height)
                            else:
                                if height > self.h_right:
                                    self.Balance(a)
                                self.h_right = max(self.h_right, height)
                        break
                    node = left_child 
                    node_value = self.__tree[node][0]
                    left_child = self.__tree[node][1]
                    right_child = self.__tree[node][2]
                elif a > node_value:
                    if right_child == -1:
                        self.__tree.append([a, -1, -1, 1])
                        self.__tree[node][2] = len(self.__tree) - 1
                        if self.__tree[node][1] == -1:
                            height = height + 1
                            if a < self.__tree[self.root][0]:
                                if height > self.h_left:
                                    self.Balance(a)
                                self.h_left = max(self.h_left, height)
                            else:
                                if height > self.h_right:
                                    self.Balance(a)
                                self.h_right = max(self.h_right, height)
                        break
                    node = right_child 
                    node_value = self.__tree[node][0]
                    left_child = self.__tree[node][1]
                    right_child = self.__tree[node][2]
                else:
                    self.__tree[node][3] = self.__tree[node][3] + 1
                    break
            
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        stack_value = self.__stack.pop()
        node = self.root
        while (stack_value != self.__tree[node][0]):
            if stack_value < self.__tree[node][0]:
                node = self.__tree[node][1]
            else:
                node = self.__tree[node][2]

        if self.__tree[node][3] > 1:
            self.__tree[node][3] = self.__tree[node][3] - 1
            return

        


    def Max(self):
        assert(len(self.__stack))
        return max(self.__stack)


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
