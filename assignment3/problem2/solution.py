#Dominick Spadafore
#Vivian Chen
#Michael Shi mxs977

from queue import PriorityQueue
import heapq
import math

"""
This is Pseudocode from class

Algorithm Dijkstra (G = (V;E), l(e) for any e 2 E, s 2 V)
    dist[v] = infinity, for any v 2 V;
    prev[v] = null, for any v in V;
    init an empty priority queue PQ;
    for any v in V: insert (PQ, v), where the priority of v is infinity;
    dist[s] = 0;
    decrease-key (PQ; s; 0);
    while (empty (PQ) = false)
        u = find-min (PQ);
        delete-min (PQ);
        for each edge (u;v) in E
            if (dist[v] > dist[u]+l(u,v))
                dist[v] = dist[u]+l(u,v);
                prev[v] = u;
                decrease-key (PQ, v, dist[v]);
            end if;
        end for;
    end while;
end algorithm;
"""

"""
class PriorityQueue:
    
    def empty(PQ):
        if (n == 0): return True
        else: return False
    
    # Incomplete
    def insert(PQ, x):
        n = n + 1
        S.append(x)
        bubble_up(S, n)
    
    # Incomplete
    def find_min(PQ):
        return S[0]

    # Incomplete
    def delete_min(PQ):
        S[0] = S[n - 1]
        n = n - 1
        sift_down(S, 1)

    # Incomplete
    def decrease_key(PQ, k, new_key):
        S[k].key = new_key
        bubble_up(S, k)
    
    # Incomplete
    def bubble_up(S, k):
        p = k/2
        if (S[k - 1].key < S[p - 1].key):
            swap(p, k)
            bubble_up(S, p)
    
    # Incomplete
    def sift_down(S, k):


    def swap(p, k):
        temp = S[p - 1]
        S[p - 1] = S[k - 1]
        S[k - 1] = temp
    """



def dijkstra(n, m, s, l, v):
    infinity = 99999

    dist = [infinity] * n
    prev = [None] * n
    #PQ = PriorityQueue()
    heap = []
    heapq.heapify(heap)

    # for any v in V: insert (PQ, v), where the priority of v is infinity
    for i in range(0, n):
        heapq.heappush(heap, i + 1)


    dist[s - 1] = 0
    #PQ.decrease_key(PQ, s, 0)

    while(heap): #PQ.empty() == False
        #u = PQ.find_min()
        u = heap[0]
        #PQ.delete_min(PQ)
        heapq.heappop(heap)
        for i in range(0, m):
            
            if (dist[v[i] - 1] > dist[u - 1] + l[i]):
                dist[v[i] - 1] = dist[u - 1] + l[i]
                prev[v[i] - 1] = u
                #PQ.decrease_key(PQ, v, dist[v - 1])

    for i in range(0, n):
        print(dist[v[i] - 1])
                

# Mainframe
line1 = input().split()
n = int(line1[0])
m = int(line1[1])
s = int(line1[2])

l = []
u = []
v = []

for i in range(0, m):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    u.append(a)
    v.append(b)
    l.append(c)
    
dijkstra(n, m, s, l, v)
