import math
import random
from matplotlib.pyplot import plot, show

def bubbleSort(list):
    itr = 0 
    for i in range(len(list)):
        itr = itr + 1
        for j in range(0, len(list)-i-1):
            itr = itr + 1
            if list[j] > list[j+1]:
                temp = list[j+1]
                list[j+1] = list[j]
                list[j] = temp
    return itr


def insertionSort(list):
    itr = 0
    for j in range(1, len(list)):
        itr = itr + 1
        key = list[j]
        i = j - 1
        while(i >= 0 and list[i] > key):
            itr = itr + 1 
            list[i+1] = list[i]
            i = i-1
        list[i+1] = key
    return itr

#====

def bucketSort(A):
    itr = 0
    n = math.ceil(len(A)/10)
    B = [list() for i in range(n)]
    for i in range(len(A)):
        B[math.floor(A[i]/10)].append(A[i])
        itr = itr + 1
    for i in range(n):
        itr = itr + insertionSort(B[i])
    A.clear()
    for i in range(n):
        A.append(B[i])
        itr = itr + 1
    return itr  

#====

def merge(A, p, q, r):
    left = A[p:q+1]
    right =A[q+1:r+1]
 
    ind = 0
    while(len(left)>0 and len(right)>0):
        if left[0] <= right[0]:
            A[p+ind] = left.pop(0)
        else:
            A[p+ind] = right.pop(0)
        ind = ind + 1
    while len(left)>0:
        A[p+ind] = left.pop(0)
        ind = ind + 1
    while len(right)>0:
        A[p+ind] = right.pop(0)
        ind = ind + 1
    return ind


def mergeSort(A, p, r):
    i = 0 
    if p < r:
        q = math.floor((p+r)/2)
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        i = i + merge(A, p, q, r)
    return i

#====

def partition(A, p, r):
        sum = 0
        x = A[p]
        j = r + 1
        i = p - 1
        while True:
            while True:
                j = j - 1
                sum = sum + 1
                if A[j] <=  x:
                    break
            while True:
                i = i + 1
                sum = sum + 1
                if A[i] >= x:
                    break
            if j > i:
                A[i], A[j] = A[j], A[i]
            else:
                #return list((j, sum))
                return j


def quickSort(A, p, r):
    sum = 0
    if p < r:
        q = partition(A, p, r)
        sum = sum + q[1]
        quickSort(A, p, q[0])
        quickSort(A, q[0] + 1, r)
    return sum

def square(n):
    return n*n

A = list(range(100))
random.shuffle(A)

B=A
print(A)
#quickSort(A, 0, len(A)-1)
#n = bucketSort(B)
n = bubbleSort(B)

print(B)

#plot(A, [square(i) for i in A])
#show()

