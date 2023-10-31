'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''
class SearchInsertPosition:
    
    def search_insert_position(self, arr, target):
        left, right = 0, len(arr)
        print(left, right)
        while left <= right:
            middle = (left + right)//2
            if arr[middle] == target:
                return middle
            elif right - left == 1:
                return right
            elif arr[middle] < target:
                left = middle
            else:
                right = middle
            
if __name__=='__main__':
    obj = SearchInsertPosition()
    a = [[1,3,5,6]]
    print(obj.search_insert_position(a, target=2))