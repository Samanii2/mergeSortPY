with open('IntegerArray.txt') as f:
    list = [int(x) for x in f]

def listSplit(A, length):
    mid = int(length / 2)
    arrA = A[0:mid]
    arrB = A[mid:length]
    return arrA, arrB


def mergeCount(a, b):
    c = []
    inversions = 0
    while ((len(a) != 0) and len(b) != 0):
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
            inversions = inversions + len(a)
    while (len(a) != 0):
        c.append(a[0])
        a.remove(a[0])
    while (len(b) != 0):
        c.append(b[0])
        b.remove(b[0])
    return c, inversions

def mergeSortCount(li):
    if len(li) == 1:
        return li, 0
    else:
        length = len(li)
        a, b = listSplit(li, length)
        a, c = mergeSortCount(a)
        b, d = mergeSortCount(b)
    sortedList, inversions = mergeCount(a, b)
    
    return sortedList, inversions
    

def countSort(A, length):
    if length == 1:
        return 0, 0
    else:
        mid = int(length / 2)
        arrA = A[0:mid]
        arrB = A[mid:length]
        a, x = countSort(arrA, mid)
        b, y = countSort(arrB, mid)
        c, z = mergeSortCount(A)

        return c, x + y + z
    
def countingInversions(A):
    length = len(A)
    return countSort(A, length)






print(countingInversions(list))
