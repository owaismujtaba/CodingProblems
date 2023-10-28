import numpy as np

'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

'''
class FibonacciNumber:
    def __init__(self):
        self.memorization = {}
        
    def calculate_fibonacchi(self,n):
        if n in self.memorization:
            return self.memorization[n]
        elif n < 2:
            return 1
        else:
            self.memorization[n] = self.calculate_fibonacchi(n-1) + self.calculate_fibonacchi(n-2)
            return self.memorization[n]
        
    
        
class Solution:
    def traverse_till_found(self,):
        pass
    def isMatch(self, s: str, p: str) -> bool:
        is_dot = '.'
        is_star = '*'
        index = 0
        
        for char in p:
            
            if char == is_star:
                index == traverse_till_found(s, p[index])
                
            if char == is_dot:
                index += 1
                continue  
            
            if s[index] == char:
                index += 1
            else:
                return False 

        return True
if __name__ == '__main__':
    obj = FibonacciNumber()
    print(obj.calculate_fibonacchi(100))
    print(obj.memorization)
    