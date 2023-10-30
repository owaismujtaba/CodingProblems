'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. 
Read this character in if it is either. 
This determines if the final result is negative or positive respectively. 
Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. 
The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). 
If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], 
then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
'''


class StringToInteger:
    def __init__(self) -> None:
        self.digits =  [str(i) for i in range(10)]
        self.state = 0
        self.sign = 1
        self.MAX = 2e31 -1
        self.MIN = -2e31
           
    def convert(self, s):
        start = 0
        end = 0
        index = 0
        while index < len(s):
            digit = s[index]
            
            if self.state == 0:
                if digit.isdigit():
                    self.state = 2
                    start = index
                elif digit == '+' or digit == '-':
                    self.state = 1
                    if digit == '-':
                        self.sign = -1
                    start = index+1
                else:
                    start = index
            elif self.state == 1:
                if digit.isdigit():
                    end = index
                    self.state = 2
                else:
                    return 0           
            elif self.state == 2:
                if digit.isdigit():
                    end = index
                else:
                    self.state = 0
                    start = index
                                            
            else:
                return 0
            index += 1
        print(number)
        number = int(s[start:end+1])
        number = number * self.sign
        
              
                
        
if __name__ == '__main__':
    obj = StringToInteger()
    res = obj.convert("w92   -987w")
    print(res)
    

'''
else:
                    if digit == '-':
                        self.sign = 1
                        self.state = 1
                        continue
                    if digit == '+':
                        self.state = 1
                        continue
                    if digit in self.digits:
                        number = number *10 + int(digit)
                        self.state = 2
                    else:
                        return ''
            elif self.state == 1:
                if digit not in self.digits:
                    return ''
                else:
                    number = number *10 + int(digit)
                    self.state = 2
                
            else:
                if digit not in self.digits:
                    break 
                else:
                    number = number *10 + int(digit)
                    #self.state = 2
        if self.sign:
            number = number * -1
            if number < self.MIN:
                return self.MIN
            else:
                return number
        return number    
'''