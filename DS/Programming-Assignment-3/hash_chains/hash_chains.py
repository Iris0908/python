# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007
    result = []

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for _ in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, ind, s):
        for query in self.elems[ind]:
            if query == s:
                #print('yes')
                self.result.append('yes')
                return
        #print('no')
        self.result.append('no')

    def write_chain(self, chain):
        #print(' '.join(chain))
        self.result.append(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            #self.write_chain(cur for cur in reversed(self.elems)
            #            if self._hash_func(cur) == query.ind)
            self.write_chain(reversed(self.elems[query.ind]))
        else:
            #try:
            #    ind = self.elems.index(query.s)
            #except ValueError:
            #    ind = -1
            ind = self._hash_func(query.s)
            if query.type == 'find':
                self.write_search_result(ind, query.s)
            elif query.type == 'add':
            #    if ind == -1:
                try:
                    self.elems[ind].index(query.s)
                except ValueError:
                    self.elems[ind].append(query.s)
            else:
            #    if ind != -1:
                try:
                    self.elems[ind].remove(query.s)
                except ValueError:
                    pass

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
    for cur in proc.result:
        print(cur)
