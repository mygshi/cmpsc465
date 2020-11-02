#Dominick Spadafore djs6744
#Vivian Chen vyc5073
#Michael Shi mxs977

import heapq

def dijkstra(n, m, s, l, E, v):
    infinity = 99999

    dist = [infinity] * n
    prev = [None] * n
    PQ = []
    heapq.heapify(PQ)

    for i in range(0, n):
        if(i == s - 1):
            heapq.heappush(PQ, (0, i + 1))
        else:
            heapq.heappush(PQ, (infinity, i + 1))
        
    dist[s - 1] = 0
    
    while(PQ):
        u = PQ[0][1]
        heapq.heappop(PQ)
        for i in range(len(E)):
            if([u, v[i]] in E):
                index = E.index([u, v[i]])
                
            else:
                continue
            if (dist[v[i] - 1] > dist[u - 1] + l[i]):
                dist[v[i] - 1] = dist[u - 1] + l[i]
                prev[v[i] - 1] = u

                if(dist[v[i] - 1] > 0):
                    heapq.heappush(PQ, (dist[v[i] - 1], v[i]))

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
