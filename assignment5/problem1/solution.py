#Dominick Spadafore djs6744
#Vivian Chen vyc5073
#Michael Shi mxs977

def DPWeighted(lst,n): 
    intervals = sorted(lst, key=lambda inter: (inter[1],inter[0]))#sorts the intervals by ending times, then starting times
    F = [0]
    for k in range(1,n+1):
        pre = binarySearch(intervals,k,0,k-1)#find the rightmost interval that doesn't overlap
        F.append(max(F[k-1],F[pre] + intervals[k][2]))
    return F[n]
    
#finds the rightmost interval that doesn't overlap
def binarySearch(A,k,a,b):
    m = int((a+b)/2)
    if(A[m][1] <= A[k][0] <= A[m+1][1]):
        return m
    elif(A[m][1]>A[k][0]):
        return binarySearch(A,k,a,m)
    else:#if(A[k][0]>A[m+1][1]):
        return binarySearch(A,k,m+1,b)

#main function
n = int(input())
intervals = [[0,0,0]]#initialize the F list so it can start with the first interval without errors
for i in range(n):
    line = input().split()
    start = int(line[0])
    terminate = int(line[1])
    value = int(line[2])
    intervals.append([start,terminate,value])
print(DPWeighted(intervals,n))