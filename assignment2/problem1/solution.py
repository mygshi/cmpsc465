length = int(input())
array = []

for i in range(0, length):
    array.append(input().split())

i = 0
j = 0
counter = 0

while i < length:
    if i < j:
        if int(array[i][0]) > int(array[j][0]):
           counter += 1
    j += 1
    if j == int(len(array)):
        i += 1
        j = i

print(counter)
