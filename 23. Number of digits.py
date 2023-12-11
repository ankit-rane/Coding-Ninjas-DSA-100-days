from os import *
from sys import *
from collections import *
from math import *

def countDigit(n: int) -> int:
    # Convert the integer to a string and calculate its length
    num_digits = len(str(n))
    return num_digits

# Example Usage
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        X = int(input())
        result = countDigit(X)
        print(result)
