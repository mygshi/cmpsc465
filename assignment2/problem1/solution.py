#Dominick Spadafore, Vivian Chen, Michael Shi
def mergeSort(arr, left, right):
    inversion_count = 0
    if left < right:
        middle = left + (right - left)//2

        inversion_count += mergeSort(arr, left, middle)
  
        inversion_count += mergeSort(arr, middle + 1, right)
  
        inversion_count += merge(arr, left, middle, right) 
        
    return inversion_count 
  
def merge(arr, left, middle, right): 
    k = left
    k1 = k2 = 0
    k3 = left
    inversion_count = 0
    size_left = middle - left + 1
    size_right = right - middle
    arr_left = []
    arr_right = []
    
    for i in range(0, size_left):
        arr_left.append(int(arr[left + i]))

    for i in range(0, size_right):
        arr_right.append(int(arr[middle + 1 + i]))
    
    while k1 < size_left and k2 < size_right: 
  
        if arr_left[k1] < arr_right[k2]: 
            arr[k] = arr_left[k1]
            k3 += 1
            k1 += 1
        else:
            arr[k] = arr_right[k2]
            if arr_left[k1] != arr_right[k2]:
                inversion_count += (middle - k3 + 1)
            k2 += 1
        k += 1
  
    while k1 < size_left: 
        arr[k] = arr_left[k1]
        k += 1
        k1 += 1
  
    while k2 < size_right: 
        arr[k] = arr_right[k2] 
        k += 1
        k2 += 1
  
    return inversion_count

# mainframe
n = input()
arr = []
arr.append(input().split())
output = mergeSort(arr[0], 0, int(n)-1)
print(output)
