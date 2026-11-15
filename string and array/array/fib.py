# a=0
# b=1
# n=int(input("Enter"))
# print(a)
# print(b)
# for i in range(n-2):
#     c=a+b
#     a=b
#     b=c
#     print(c)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter: "))
fib_series = [fibonacci(i) for i in range(n)]
print(fib_series) 
