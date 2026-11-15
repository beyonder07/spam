# class Node:
#     def __init__(self,data):
#         self.data = data 
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def insert(self,data):
#         new_node=Node(data)
#         new_node.next=self.head
#         self.head=new_node
#     def search(self,target):
#         temp=self.head
#         while temp:
#             if temp.data == target:
#                 return f"element{target}found"
#             temp = temp.next
#         return f"not found"
#     def display(self):
#         temp=self.head
#         while temp:
#             print(temp.data,end="->")
#             temp=temp.next
#         print("None")
# ll=LinkedList()
# n=int(input("enter"))
# for _ in range(n):
#     value=int(input("number"))
#     ll.insert(value)
# print("Linked list:")
# ll.display()
# search_value=int(input("target"))
# print(ll.search(search_value))
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def min_max(self):
        if not self.head:  # If the list is empty
            return "The list is empty."
        
        min_value = max_value = self.head.data  # Start with the first element's value
        temp = self.head.next
        
        while temp:
            if temp.data < min_value:
                min_value = temp.data
            if temp.data > max_value:
                max_value = temp.data
            temp = temp.next
        
        return f"Min: {min_value}, Max: {max_value}"
    def square(self):
        temp=self.head
        while temp:
            temp.data=temp.data**2
            temp=temp.next


    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

ll = LinkedList()
n = int(input("Enter the number of elements: "))
for _ in range(n):
    value = int(input("Enter a number: "))
    ll.insert(value)

print("Linked List:")

# Finding the minimum and maximum values
print(ll.min_max())
ll.square()
print("Linked list after squaring elements:")
ll.display()



