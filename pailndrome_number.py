'''
Given an integer x, return true if x is a 
palindrome, and false otherwise.
'''
class CheckPalindrome:
    
    def check_palindrome(self, x):
        print(x)
        if x<0:
            return False
        x = str(x)
        start = 0
        end = len(x)-1
        
        while start < end:
            if x[start] == x[end]:
                start += 1
                end -= 1
            else:
                return False
        
        return True
    
if __name__=='__main':
    obj = CheckPalindrome()
    res = obj.check_palindrome(121)
    print(res)
        