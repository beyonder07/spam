# double=[x**2 for x in range(1,11)]
# # for i in range(1,11):
# #     double.append(i*2)
# print(double)
# fruits=["apple","banana","cherry"]
# fruits=[fruit[0] for fruit in fruits]
# print(fruits)
nums=list(map(int,input("enter").split()))
pos=[i for i in nums if i>0]
print(pos)
negs=[i for i in nums if i<0]
print(negs)
even={i for i in nums if i%2==0}
print(even)
print(nums) 