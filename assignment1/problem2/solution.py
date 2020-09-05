length = input()
ls = input().split()

def merge(l1, l2):
    first_pointer = second_pointer = 0
    len1 = len(l1)
    len2 = len(l2)
    totalLength = len1 + len2
    third = []
    for i in range(0, totalLength):
        if len1 == first_pointer:
            third.append(int(l2[second_pointer]))
            second_pointer += 1
        elif len2 == second_pointer:
            third.append(int(l1[first_pointer]))
            first_pointer += 1
        elif int(l1[first_pointer]) <= int(l2[second_pointer]):
            third.append(int(l1[first_pointer]))
            first_pointer += 1
        else:
            third.append(int(l2[second_pointer]))
            second_pointer += 1
    return third

def mergeSort(lt):
    if len(lt) <= 1:
        return lt
    n = int(len(lt)/2)
    sort1 = mergeSort(lt[:n])
    sort2 = mergeSort(lt[n:])
    return merge(sort1, sort2)

arrayString = ""
for i in mergeSort(ls):
    arrayString += (str(i) + " ")
print(arrayString)
