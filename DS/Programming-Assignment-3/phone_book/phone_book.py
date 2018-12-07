# python3
import random

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

class Hash_table:
    def __init__(self, p):
        self.p = p
        self.a = random.randint(0, p)
        self.b = random.randint(0, p)
        self.m = 2
        self.contacts = [[] for _ in range(self.m)]
        self.size = 0


    def hash_key(self, number):
        return (((self.a * number + self.b) % self.p) % self.m)


    def refresh(self):
        self.a = random.randint(0, self.p)
        self.b = random.randint(0, self.p)
        self.m = self.m * 2
        contacts = self.contacts.copy()
        self.contacts.clear()
        self.contacts = [[] for _ in range(self.m)]

        for contact in contacts:
            for cur_query in contact:
                self.contacts[self.hash_key(cur_query.number)].append(cur_query)


    def add(self, cur_query):
        if self.size == self.m:
            self.refresh()

        key = self.hash_key(cur_query.number)
        for contact in self.contacts[key]:
            if contact.number == cur_query.number:
                contact.name = cur_query.name
                return

        self.contacts[key].append(cur_query)
        self.size = self.size + 1


    def delet(self, number):
        index = 0
        key = self.hash_key(number)
        for contact in self.contacts[key]:
            if contact.number == number:
                break
            index = index + 1

        if len(self.contacts[key]) != index:
            self.contacts[key].pop(index)


    def find(self, number):
        key = self.hash_key(number)
        for contact in self.contacts[key]:
            if contact.number == number:
                return contact.name
        return 'not found'


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    hash_table = Hash_table(10000000)
    # Keep list of all existing (i.e. not deleted yet) contacts.
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            hash_table.add(cur_query)
        elif cur_query.type == 'del':
            hash_table.delet(cur_query.number)
        else:
            result.append(hash_table.find(cur_query.number))
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

