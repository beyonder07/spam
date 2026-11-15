# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# class Doubly:
#     def __init__(self):
#         self.head=None
# L=Doubly()
# n1=Node(10)
# L.head=n1
# n2=Node(20)
# n1.next=n2
# n2.prev=n1
# n3=Node(30)
# n2.next=n3
# n3.prev=n2
# n3.next=None
# if L.head is None:
#     print("empty")
# else:
#     temp=L.head
#     while temp:
#         print(temp.data,end="->")
#         temp=temp.next
#     print("None")
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Doubly:
    def __init__(self):
        self.head=None
    def end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev = temp
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")
L=Doubly()
custom=[10,20,30,40,50]
for i in custom:
    L.end(i)
print("Doubly linked list:")
L.display()