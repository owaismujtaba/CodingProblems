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
    
def merge_two_lists(l1, l2):
        
    head = ListNode(0)
    temp = head
    while l1 or l2:
        if l1 and l2:
            
            if l1.val <= l2.val:
                temp.next = ListNode(l1.val)
                print('l1',l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                print('l2',l2.val)
                l2 = l2.next
            
            temp = temp.next
            print(temp.val)    
        elif l1:
            temp.next = l1
            return head
        else:
            temp.next = l2
            return head
                
        return head.next

        
        
def create_list(n):
    numbers =np.random.randint(0, 10, size=n)
    head = ListNode(numbers[0])
    temp = head
    for i in range(n):
        temp.next = ListNode(numbers[i])
        temp = temp.next
        
    return head
def show_list(head):
    temp = head
    items = []
    while temp:
        items.append(temp.val)
        temp = temp.next
    print(items)
    
def create_list_from_list(items):
    head = ListNode(0)
    temp = head
    for item in items:
        temp.next = ListNode(item)
        temp = temp.next
    return head.next

if __name__=='__main__':
    a = [1,3,5,7]
    b = [2,2,4,5,6,9]
    l1 = create_list_from_list(a)
    l2 = create_list_from_list(b)
    
    show_list(l1)
    show_list(l2)
    l3 = merge_two_lists(l1,l2)
    show_list(l3)
    print(a[-1])