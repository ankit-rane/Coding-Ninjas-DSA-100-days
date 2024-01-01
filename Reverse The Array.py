from os import *
from sys import *
from collections import *
from math import *

def reverseArray(arr, m):
    newArr = arr[:m+1]+arr[m+1:][::-1]
    return newArr
    pass
