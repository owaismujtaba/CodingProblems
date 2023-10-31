'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
'''
class AddDigits:
    
    def addDigits(self, num):
        
        while True:
            result = 0
            print(num)
            while num > 0:
                result = result+ num%10
                num = num//10
            if result > 9:
                num = result
            else:
                return result
            
            
obj = AddDigits()
print(obj.addDigits(21293))
                
                
