# a=5
# b=6
# s=a+b
# print(s)
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=input("Enter the operation: ")
def switch_case(a,b,c):
    match c:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
result = switch_case(a, b, c)
print("Result:", result)
