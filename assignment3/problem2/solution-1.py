#Dominick Spadafore djs6744
#Vivian Chen vyc5073
#Michael Shi mxs977

class Graph(): 
  
    def __init__(self, n): 
        self.V = n 
        self.graph = [[0 for i in range(n)]  
                    for j in range(n)]

    def find_min(self, dist, prev):

        min = 999999
        index = 0

        for v in range(self.V):
            if dist[v] < min and prev[v] == None:
                min = dist[v]
                index = v

        return index

    def dijkstra(self, s): 

        dist = [999999] * self.V
        dist[s] = 0
        prev = [None] * self.V 
  
        for cout in range(self.V): 
  
            u = self.find_min(dist, prev)
  
            prev[u] = True
  
            for v in range(self.V): 
                if self.graph[u][v] > 0 and prev[v] == None and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v]
  
        for i in range(self.V):
            if(dist[i] == 999999):
                dist[i] = -1
            print(dist[i]) 
  
# Mainframe
line1 = input().split()
n = int(line1[0])
m = int(line1[1])
s = int(line1[2])
g = Graph(n)

for i in range(0, m):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    g.graph[a-1][b-1] = c

g.dijkstra(s-1)
