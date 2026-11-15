# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, data):
#         self.stack.append(data)

#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         return "Stack is empty"

#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         return "Stack is empty"

#     def is_empty(self):
#         return len(self.stack) == 0

#     def display(self):
#         print("Stack (Top -> Bottom):", self.stack[::-1])

# # Example usage
# s = Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.display()  
# print("Top Element:", s.peek())  
# s.pop()
# s.display()
# print("Stack Empty?", s.is_empty())
*********GREATER*************
# def nextGreaterElement(arr):
#     stack = []
#     result = [-1] * len(arr)

#     for i in range(len(arr) - 1, -1, -1):
#         while stack and stack[-1] <= arr[i]:
#             stack.pop()
#         if stack:
#             result[i] = stack[-1]
#         stack.append(arr[i])
    
#     return result

# print(nextGreaterElement([4, 5, 2, 10]))  # Output: [5, 10, 10, -1]
***********PARANTHESIS*************
# def isValid(s):
#     stack = []
#     mapping = {')': '(', '}': '{', ']': '['}
    
#     for char in s:
#         if char in mapping:
#             top = stack.pop() if stack else '#'
#             if mapping[char] != top:
#                 return False
#         else:
#             stack.append(char)
    
#     return not stack

# print(isValid("{[()]}"))  # Output: True
***********MIN STACK*************
# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.minStack = []

#     def push(self, val):
#         self.stack.append(val)
#         if not self.minStack or val <= self.minStack[-1]:
#             self.minStack.append(val)

#     def pop(self):
#         if self.stack.pop() == self.minStack[-1]:
#             self.minStack.pop()

#     def top(self):
#         return self.stack[-1]

#     def getMin(self):
#         return self.minStack[-1]

# s = MinStack()
# s.push(2)
# s.push(1)
# s.push(3)
# print(s.getMin())  # Output: 1
# ********REVERSE*******
# def insert_at_bottom(stack, item):
#     if not stack:
#         stack.append(item)
#         return
#     temp = stack.pop()
#     insert_at_bottom(stack, item)
#     stack.append(temp)

# def reverse_stack(stack):
#     if not stack:
#         return
#     temp = stack.pop()
#     reverse_stack(stack)
#     insert_at_bottom(stack, temp)


# stack = [1, 2, 3, 4, 5]
# reverse_stack(stack)
# print(stack)  
***********Unique Characters*************

def find_first_non_repeating_char_index(s):
    stack = []
    seen = set()
    for char in s:
        if char not in seen:
            stack.append(char)
            seen.add(char)
        else:
            if char in stack:
                stack.remove(char)
    for index, char in enumerate(s):
        if char in stack:
            return index
    
    return -1

user_input = input("Enter a string: ")
result = find_first_non_repeating_char_index(user_input)
print("Index of first non-repeating character:", result)
