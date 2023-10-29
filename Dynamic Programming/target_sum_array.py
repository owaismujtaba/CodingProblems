
class TargetSum:
    def __init__(self):
        self.memorization = {}
        
    def target_sum_with_reuse_of_elements(self,arr, target):
        if target in self.memorization:
            return self.memorization[target]
        if target == 0:
            return True
        if target < 0:
            return False
        
        for num in arr:
            remainder = target - num
            if self.target_sum(arr, remainder):
                self.memorization[remainder] = True
                return True 
        return False
    
    def elements_with_target_sum(self,arr, target):
        if target in self.memorization:
            return self.memorization[target]
        if target == 0:
            return True
        if target < 0:
            return False
        
        for num in arr:
            remainder = target - num
            if self.target_sum(arr, remainder):
                self.memorization[remainder] = True
                return True
        
        return False

import numpy as np
import pdb
class Solution:
    def minGroupsForValidAssignment(self, nums):
        arr = np.array(nums)
        #pdb.set_trace()
        unique = np.unique(arr)
        value_counts = np.unique(arr, return_counts=True)
        print(value_counts)
        return ''
        
class Solution1:
    def minSum(self, nums1, k):
        nums1 = nums1.sort(reverse = True)
        if nums1[-1]> k:
            return 0
        else:
            
        return 0          
if __name__ == '__main__':
    obj = Solution1()
    x = [8,13,15,18,0,18,0,0,5,20,12,27,3,14,22,0]
    y = [29,1,6,0,10,24,27,17,14,13,2,19,2,11]
    print(obj.minSum(x,y))
