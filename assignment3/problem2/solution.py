#Dominick Spadafore
#Vivian Chen
#Michael Shi mxs977

from queue import PriorityQueue
import heapq
import math

def dijkstra(n, m, s, l, E, v):
    infinity = 99999

    dist = [infinity] * n
    prev = [None] * n
    #PQ = PriorityQueue()
    PQ = []
    heapq.heapify(PQ)

    # for any v in V: insert (PQ, v), where the priority of v is infinity
    for i in range(0, n):
        heapq.heappush(PQ, (infinity, i + 1))
        
    dist[s - 1] = 0
    #PQ.decrease_key(PQ, s, 0)
    #heapq._siftdown(PQ, s, 0)
    print(PQ)
    
    while(PQ): #PQ.empty() == False
        #u = PQ.find_min()
        u = PQ[0][1]
        #PQ.delete_min(PQ)
        heapq.heappop(PQ)
        for i in range(len(E)):
            print("i =", i)
            print("(u, v) =", u, v[i])
            if([u, v[i]] in E):
                index = E.index([u, v[i]])
                print("(u, v) =", u, v[index], "length =", l[index])
                print("index =", index) 
                
            else:
                continue

            if (dist[v[i] - 1] > dist[u - 1] + l[index]):
                dist[v[i] - 1] = dist[u - 1] + l[index]
                prev[v[i] - 1] = u

    for i in range(0, len(dist)):
        print(dist[i])

# Mainframe
line1 = input().split()
n = int(line1[0])
m = int(line1[1])
s = int(line1[2])

l = []
u = []
v = []
E = []

for i in range(0, m):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    u.append(a)
    v.append(b)
    l.append(c)
    E.append([a,b])

dijkstra(n, m, s, l, E, v)
