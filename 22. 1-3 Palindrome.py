from typing import List

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def palindrome13(s: str) -> int:
    n = len(s)
    
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            part1 = s[:i]
            part2 = s[i:j]
            part3 = s[j:]
            
            new_str = part1 + part3
            
            if is_palindrome(new_str):
                return 1
    
    return 0
