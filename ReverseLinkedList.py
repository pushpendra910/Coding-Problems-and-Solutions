from locale import currency
from re import L


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
    
    def push(self, new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def printL(self):
        temp=self.head
        while(temp):
            print (temp.data,end=' ')
            temp=temp.next

    def reverse(self):  
        prev=None
        current=self.head
        while(current):
            next=current.next
            current.next=prev
            prev=current
            current=next

        self.head=prev

    def reverse_recursive(self,head):
        if head is None or head.next is None:
            return head

        rest=self.reverse_recursive(head.next)

        head.next.next=head
        head.next=None
        return rest



ll=LinkedList()
ll.push(20)
ll.push(45)
ll.push(60)
ll.push(80)
ll.push(90)

ll.printL()
print()
ll.reverse_recursive(ll.head)
ll.printL()

