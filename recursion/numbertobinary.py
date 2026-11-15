# n=int(input("Enter a number: "))
# def fun(n):
#     if n==0:
#         return
#     fun(n//2)
#     print(n%2)
# fun(n)
# n=12
# d=0
# s=0
# while n>0:
#     s=s+n%10
#     n=n//10
# print(s)
# def fun(n):
#     if n<10:
#         return n
#     return n%10 + fun(n//10)
# print(fun(12))

def fun(n):
    if n==0:
        return " "
    fun(n-1)
    print(n,end=" ")
print(fun(5))
        