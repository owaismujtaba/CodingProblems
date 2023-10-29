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

if __name__ == '__main__':
    obj = MaxMinOp()
    print(obj.maximizeMinimizeOperations(12))
    print(obj.memo)