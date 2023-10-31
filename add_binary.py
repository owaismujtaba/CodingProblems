'''
Given two binary strings a and b, return their sum as a binary string.
'''

class AddBinary:
    def add_binary(self, a: str, b: str) -> str:
        
        a_index = len(a)
        b_index = len(b)
        if a_index< 1:
            return b
        if b_index < 1:
            return a
        res = ''
        carry = 0
        max_size = a_index if a_index>b_index else b_index
        for i in range(max_size):
            if a_index<1:
                x = 0
            else:
                x = int(a[a_index-1])
            if b_index <1:
                y = 0
            else:
                y = int(b[b_index-1])
           
            digit =  x + y + carry
            if digit == 3:
                carry = 1
                digit = '1'
            elif digit == 2:
                carry = 1
                digit = '0'
            elif digit == 1:
                carry = 0
                digit = '1'
            else:
                digit = '0'
                carry = 0
            res = digit + res
            a_index -= 1
            b_index -= 1
        if carry:
            return '1'+res   
            
        return res
    
    def add_binary_efficient(self, a, b):
        a_index = len(a)
        b_index = len(b)
        sum_binary = ''
        carry = 0
        while a_index>0 or b_index>0 or carry:
                if a_index>0:
                    carry += int(a[a_index-1])
                    a_index -= 1
                                    
                if b_index>0:
                    carry += int(b[b_index-1])
                    b_index -=1
                
                sum_binary = str(carry%2) + sum_binary
                carry = carry//2
                if not carry and not a_index:
                    sum_binary = b[:b_index] + sum_binary
                    return sum_binary 
                if not carry and not b_index:
                    sum_binary = a[:a_index] + sum_binary
                    return sum_binary 

        return sum_binary
        
    
obj = AddBinary()
print(obj.add_binary_efficient('100', '110010'))