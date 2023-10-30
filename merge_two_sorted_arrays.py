'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing 
together the nodes of the first two lists.
'''
from random import randint
import numpy as np

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
    
    def merge_two_lists

        
        
def create_list(numbers):
    numbers =np.random.randint(0, 10, size=10)
    head = ListNode(numbers[0])
    temp = head
    for i in range(1, n):
        temp.next = ListNode(numbers[i])
        temp = temp.next
        
    return head
def show_list(head):
    temp = head
    while temp:
        print(temp.val)
        temp = temp.next
        
        
if __name__=='__main__':
    l1 = create_list(10)
    l2 = create_list(5)
    
    show_list(l1)