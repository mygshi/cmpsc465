#Dominick Spadafore
#Vivian Chen
#Michael Shi mxs977

class PriorityQueue(s):
    
    S[0] = s

    def empty():
        if (n == 0): return True
        else: return False
    
    # Incomplete
    def insert(x):
        n = n + 1
        S[n] = x
        bubble_up(S, n)
    
    # Incomplete
    def find_min(PQ):
        return S[0]

    # Incomplete
    def delete_min():
        S[0] = S[n - 1]
        n = n - 1
        sift_down(S, 1)

    # Incomplete
    def decrease_key(k, new_key):
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



def dijkstra(n, m, s):
    infinity = 99999

    dist = [infinity] * n
    prev = [None] * n
    PQ = PriorityQueue(s)


    # for any v in V: insert (PQ, v), where the priority of v is infinity
    for i in range(0, n):
        PQ.insert(n + 1)

    dist[s - 1] = 0
    print(dist)
    PQ.decrease_key(s, 0)

    while(PQ.empty() == False):
        u = PQ.find_min()
        PQ.delete_min()
        for i in range(0, m):
            if (dist[v - 1] > dist[u - 1] + c):
                dist[v - 1] = dist[u - 1] + c
                prev[v - 1] = u
                PQ.decrease_key(v, dist[v - 1])

# Mainframe
line1 = input().split()
n = int(line1[0])
m = int(line1[1])
s = int(line1[2])

dijkstra(n, m, s)

# Incomplete
for i in range(0, m):
    c = 1
