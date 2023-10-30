'''
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
then return 0.
'''

class ReverseInteger:
    def __init__(self) -> None:
        self.MAX = 2**31 -1
        self.MIN = -2**32
        print(self.MAX, self.MIN)
        
    def reverse_integer(self, x):
        number = 0
        sign = 1
        if x <  0:
            sign = -1
        x = abs(x)
        while x>0:
            number = number*10 + x%10
            x = x//10
            if number > self.MAX:
                return 0
        number = number * sign
        if number < self.MIN:
            return 0
        return number
    
if __name__ == '__main__':
    obj = ReverseInteger()
    print(obj.reverse_integer(1563847412))