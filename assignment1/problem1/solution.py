first = input()
second = input()
l1 = first.split()
l2 = second.split()
len1 = int(l1[0])
len2 = int(l2[0])
l1 = l1[1:]
l2 = l2[1:]
third = []
length = len1 + len2


def merge_sort(l1, l2):
    first_pointer = second_pointer = 0
    for i in range(0, length):
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
    third.insert(0, length)
    print(' '.join(str(x) for x in third))

merge_sort(l1, l2)