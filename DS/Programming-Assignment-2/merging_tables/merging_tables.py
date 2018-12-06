# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
#rank = [1] * n
#parent = list(range(0, n))
node = []
ans = max(lines)

for row in lines:
    node.append([-1, 1, row])

def getParent(table):
    # find parent and compress path
    parent = []
    root = table
    while node[root][0] != -1:
        parent.append(root)
        root = node[root][0]

    for child in parent:
        node[child][0] = root

    return root

def merge(destination, source):
    global ans
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False

    #print('00 destination, realSource:', realDestination+1, realSource+1, node[realDestination][2], node[realSource][2], ans)
    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    if node[realDestination][1] >= node[realSource][1]:
        node[realDestination][2] = node[realDestination][2] + node[realSource][2]
        if node[realDestination][1] == node[realSource][1]:
            node[realDestination][1] = node[realDestination][1] + 1
        node[realSource][0] = realDestination
        node[realSource][1] = 0
        ans = max(ans, node[realDestination][2])
        #print('11 destination << realSource:', realDestination+1, realSource+1, node[realDestination][2], node[realSource][2], ans)
        return True

    node[realSource][2] = node[realDestination][2] + node[realSource][2]
    node[realDestination][0] = realSource
    node[realDestination][1] = 0
    ans = max(ans, node[realSource][2])
    #print('22 destination >> realSource:', realDestination+1, realSource+1, node[realDestination][2], node[realSource][2], ans)
    return True

result = []
for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    result.append(ans)
    #print(ans)

for number in result:
    print(number)
    
