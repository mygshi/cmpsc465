#Dominick Spadafore djs6744
#Vivian Chen vyc5073
#Michael Shi mxs977

<<<<<<< HEAD
from queue import PriorityQueue
import heapq
import math

def dijkstra(n, m, s, l, E, v):
    infinity = math.inf

    dist = [infinity] * n
    prev = [None] * n
    #PQ = PriorityQueue()
    PQ = []
    heapq.heapify(PQ)

    # for any v in V: insert (PQ, v), where the priority of v is infinity
    for i in range(0, n):
        if(i == s - 1):
            heapq.heappush(PQ, (0, i + 1))
        else:
            heapq.heappush(PQ, (infinity, i + 1))

    #print(PQ)
    #heapq.heappush(PQ, (0, 5))
    #print(PQ)
        
    dist[s - 1] = 0
    #PQ.decrease_key(PQ, s, 0)
    #heapq._siftdown(PQ, s, 0)
    #print(PQ)
    
    while(PQ): #PQ.empty() == False
        #u = PQ.find_min()
        u = PQ[0][1]
        #PQ.delete_min(PQ)
        heapq.heappop(PQ)
        #print(PQ)
        for i in range(len(E)):
            #print("(u, v) =", u, v[i])
            if([u, v[i]] in E):
                index = E.index([u, v[i]])
                #print("(u, v) =", u, v[index], "length =", l[index])
                #print("index =", index) 
                
            else:
                #index = i
                continue
            
            
            if (dist[v[i] - 1] > dist[u - 1] + l[index]):
                dist[v[i] - 1] = dist[u - 1] + l[index]
                prev[v[i] - 1] = u
                #print(PQ)
                if(dist[v[i] - 1] > 0):
                    heapq.heappush(PQ, (dist[v[i] - 1], v[i]))
                

    for i in range(0, len(dist)):
=======
def find_min(dist, prev):

        min = 999999
        index = 0

        for v in range(n):
            if dist[v] < min and prev[v] == None:
                min = dist[v]
                index = v

        return index

def dijkstra(s, n, graph): 

    dist = [999999] * n
    dist[s] = 0
    prev = [None] * n 
  
    for cout in range(n): 
  
        u = find_min(dist, prev)
  
        prev[u] = True
  
        for v in range(n): 
            if graph[u][v] > 0 and prev[v] == None and dist[v] > dist[u] + graph[u][v]: 
                dist[v] = dist[u] + graph[u][v]
  
    for i in range(n):
        if(dist[i] == 999999):
            dist[i] = -1
>>>>>>> 30858ad9517182c41b760a19a492892718f93438
        print(dist[i])

# Mainframe
line1 = input().split()
n = int(line1[0])
m = int(line1[1])
s = int(line1[2])
graph = []
for i in range(0, n):
    graph.append([0]*n)

for i in range(0, m):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    graph[a-1][b-1] = c

dijkstra(s-1, n, graph)
