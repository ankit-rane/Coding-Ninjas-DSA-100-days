from os import *
from sys import *
from collections import *
from math import *

def printName(s):
    count = 0
    if len(s)<=10000:
        while count < 5:
            print(s)
            count += 1
    else:
        return 0
    pass
