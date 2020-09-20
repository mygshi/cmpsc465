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
    if float(points[i][1]) < lowestY:
        lowestY = float(points[i][1])
        pointOfLowY = i
        lowestX = float(points[i][0])
    if float(points[i][0]) <= leftmostX:
        leftmostX = float(points[i][0])
    if float(points[i][0]) >= rightmostX:
        rightmostX = float(points[i][0])

#sort with angles
convert = 180/3.1415
for i in range(0,length):
    y = lowestY-float(points[i][1])
    x = lowestX-float(points[i][0])

    angle = 0
    if x==0:
        angle = 0
    elif float(points[i][0]) < lowestX:
        angle = 180-math.atan(y/-x) * convert
    else:
        angle = math.atan(y/x) * convert

    points[i].insert(0,angle)

points.sort()
#graham-scan
stack = []
stack.append(points[0][1:])
stack.append(points[1][1:])
stack.append(points[2][1:])

for i in range(3, length):
    while stack:
        print("stack:",stack)
        top = len(stack)-1
        top2 = top-1
        #right hand rule
        vec1X = (float(stack[top2][0])-float(stack[top][0]))
        vec1Y = (float(stack[top2][1])-float(stack[top][1]))
        vec2X = float(points[i][1])-float(stack[top][0])
        vec2Y = float(points[i][2])-float(stack[top][1])

        crossproduct = vec1X * vec2Y - vec1Y * vec2X
        #crossproduct of a and b determines "turning right or left"
        if crossproduct > 0:
            stack.pop()
            top-= 1
            top2 -= 1
        else:
            break

    stack.append(points[i][1:])

#find leftmost and rightmost
for i in range(0, len(stack)):
    if leftmostX == float(stack[i][0]):
        leftmost = i
    if rightmostX == float(stack[i][0]):
        rightmost = i

upper = 0
lower = 2
for i in range(0, len(stack)):
    if i >= rightmost and i <= leftmost:
        upper += 1
    else:
        lower += 1
print(upper,lower)
