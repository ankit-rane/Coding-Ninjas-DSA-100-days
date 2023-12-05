from os import *
from sys import *
from collections import *
from math import *

from typing import *

def kReplacement(n : int, k : str, str : str) -> str:
    return ''.join(k if s.isdigit() and is_prime(int(s)) else s for s in str)

def is_prime(n):
    """Check if a number is prime."""
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))
