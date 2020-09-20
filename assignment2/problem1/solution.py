length = int(input())
array = []

array.append(input().split())
    
i = 0
j = 0
counter = 0

while i < length:
    if i < j:
        if int(array[0][i]) > int(array[0][j]):
           counter += 1
    j += 1
    if j == int(length):
        i += 1
        j = i

print(counter)
