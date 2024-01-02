from os import *
from sys import *
from collections import *
from math import *

def firstPos(arr,n,k):
    low = 0
    high = n-1
    first = -1
    while low <=high:
        mid = (low+high)//2
        if arr[mid] == k:
            first = mid 
            high = mid-1
        elif arr[mid] > k:
            high = mid-1
        else:
            low = mid+1
    return first 

def secondPos(arr,n,k):
    low = 0
    high = n-1
    last = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == k:
            last = mid
            low = mid+1
        elif arr[mid] > k:
            high = mid-1
        else:
            low = mid+1
    return last 

def firstAndLastPosition(arr, n, k):
    f = firstPos(arr,n,k)
    if f==-1:
        return (-1,-1)
    s = secondPos(arr,n,k)
    return (f,s)
