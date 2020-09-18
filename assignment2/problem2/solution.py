#Vivian Chen, Michael Shi, Dominick Spadafore
import math

length = int(input())
points = []

#getting the lowest point while also extracting data from input
lowestY = 9999
pointOfLowY = None
leftmost = None
leftmostX = 999999
rightmost = None
rightmostX = -9999999
for i in range(0, length):
    points.append(input().split())
    if float(points[i][1]) <= lowestY:
        lowestY = float(points[i][1])
        pointOfLowY = i

    if float(points[i][0]) <= leftmostX:
        leftmostX = float(points[i][0])
    if float(points[i][0]) >= rightmostX:
        rightmostX = float(points[i][0])


#sort with angles
offset = 3.1415/2
for i in range(0,length):
    y = float(points[pointOfLowY][1])-float(points[i][1])
    x = float(points[pointOfLowY][0])-float(points[i][0])

    angle = math.atan2(y,x)
    if angle < 0:
        angle = abs(angle) + offset
    points[i].insert(0,angle)

points.sort()

#graham-scan
stack = []
stack.append(points[1])
stack.append(points[2])
stack.append(points[3])

for i in range(4, length):
    while not stack:
        #right hand rule
        slope1 = (point[i-1][2]-point[i-2][2])/(point[i-1][1]-point[i-2][1])
        slope2 = (point[i][2]-point[i-1][2])/(point[i][1]-point[i-1][1])

        if slope1 < slope2:
            stack.pop()
        else:
            break
    stack.append(points[i])

print(leftmostX,rightmostX)
#find leftmost and rightmost
for i in range(0, len(stack)):
    print(stack[i])
    if leftmostX == float(stack[i][1]):
        leftmost = i
    if rightmostX == float(stack[i][1]):
        rightmost = i

upper = 0
lower = 0
for i in range(0, len(stack)):
    if i >= rightmost and i <= leftmost:
        upper += 1
    else:
        lower += 1
print(upper,lower)
