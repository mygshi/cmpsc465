#Dominick Spadafore djs6744
#Vivian Chen vyc5073
#Michael Shi mxs977

# Mainframe
G = []
line1 = input().split()
n = int(line1[0])
m = int(line1[1])

for i in range (0, m):
    line = input().split()
    u = int(line[0])
    v = int(line[1])
    w = int(line[2])
    G.append([u, v, w])

# find Algorithm
def find(parent, x):
    while( parent[x] != x ):
        x = parent[x]
    return x

# union Algorithm
def union(parent, height, x, y):
    rx = find(parent, x)
    ry = find(parent, y)
 
    if( height[rx] < height[ry] ):
        parent[rx] = ry
    elif( height[rx] > height[ry] ):
        parent[ry] = rx
    else:
        parent[rx] = ry
        height[ry] += 1
 
# Kruskal Algorithm
def Kruskal(*G, n, m):
    result = []
    i = 0
    e = 0
    G = G[0]
    G = sorted(G, key=lambda item: item[2])
    
    parent = []
    height = []
    for v in range(0, n):
        parent.append(v)
        height.append(1)

    while( e < n - 1 ):
        u, v, w = G[i]
        i = i + 1
        ru = find(parent, u - 1)
        rv = find(parent, v - 1)
        if ru != rv:
            e = e + 1
            result.append([u, v, w])
            union(parent, height, ru, rv)
        
    edgeSum = 0
    for u, v, w in result:
        edgeSum += w
    print( edgeSum )

# Calling the Kruskal Algorithm
Kruskal(G, n=n, m=m)
