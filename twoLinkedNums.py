#You are given two non-empty linked lists representing two non-negative integers.
#The digits are stored in reverse order and each of their nodes contain a single digit.
#Add the two numbers and return it as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Doesn't work yet, it is close though

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        strReturn = str(self.head.data)
        curr_node = self.head
        while (curr_node.next != None):
            strReturn = strReturn + " -> " + str(curr_node.data)
            next_node = curr_node.next
            curr_node = next_node
        return strReturn

def sumLinkedLists(linked1,linked2):
    sum = collapseLinkedList(linked1) + collapseLinkedList(linked2)
    return convertNumToLinkedList(sum)

def collapseLinkedList(linked_list):
    num = ""
    next_node = linked_list.head
    while (next_node.next != None):
        num = num + str(next_node.data)
        next_node = next_node.next
    return num

def convertNumToLinkedList(num):
    new_list = LinkedList()
    curr_node = ""

    for digit in num:
        if (num.index(digit) == 0):
            new_list.head=Node(digit)
            curr_node = new_list.head
        else:
            curr_node.next = Node(digit)
            curr_node = curr_node.next
    return new_list

if __name__=="__main__":
    num1 = LinkedList()
    num1.head=Node(1)
    second = Node(1)
    third = Node(1)
    num1.head.next = second
    second.next = third
    num2 = LinkedList()
    num2.head=Node(1)
    fourth = Node(1)
    fifth = Node(1)
    num2.head.next=fourth
    fourth.next = fifth
    print (sumLinkedLists(num1,num2))
