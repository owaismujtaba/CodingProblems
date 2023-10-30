class MaxMinOp:
    def __init__(self):
        self.memo ={}
        self.operations = {}
        self.operations = [3, 1]
    def maximizeMinimizeOperations(self, target):
        if target in self.memo:
            return self.memo[target]
        if target == 1:
            return []
        if target < 1:
            return None
        for operation in self.operations:
            if operation == 3:
                if target%3 == 0:
                    result = self.maximizeMinimizeOperations(target//3)
                    result.append('Operation Multiply')
                    self.memo[target] = result
                    return result
                else:
                    result = self.maximizeMinimizeOperations(target-1)
                    result.append('Operation Add')
                    self.memo[target] = result
                    return result
                    
            
        return None
    
    def optimize_operations(self, target):
        optimized_op = []
        if self.memo[target] != None:
            operations = self.memo[target][::-1]
            right = 0
            left = 0
            counter = 0
            while right < len(operations): 
                if operations[left] == operations[right]:
                    counter += 1
                    right += 1
                else:
                    result = operations[left] + ' '+ str(counter) + ' times'
                    counter = 0
                    optimized_op.append(result)
                    left = right
            return optimized_op
                    

if __name__ == '__main__':
    obj = MaxMinOp()
    print(obj.maximizeMinimizeOperations(10))
    #print(obj.memo)
    print(obj.optimize_operations(10))