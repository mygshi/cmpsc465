#Dominick Spadafore
#Vivian Chen
#Michael Shi mxs977

line1 = input().split()
n = int(line1[0])
m = int(line1[1])
s = int(line1[2])

infinity = 99999

dist = [infinity] * n
prev = [None] * n
PQ = PriorityQueue

# for any v in V: insert (PQ, v), where the priority of v is infinity
# dist[s] = 0
# decrease-key (PQ, s, 0)

while(PQ.empty() == False):
    # u = findmin(PQ)
    # delete-min(PQ)
    for i in range(0, m):
        if (dist[v - 1] > dist[u - 1] + c):
            dist[v - 1] = dist[u - 1] + c
            prev[v - 1] = u
            #decrease-key(PQ, v, dist[v]
