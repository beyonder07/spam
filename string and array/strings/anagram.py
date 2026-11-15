str1=input("enter: ")
str2=input("enter: ")

# if sorted(str1)==sorted(str2):
#     print("Anagrams")
# else:
#     print("Not Anagrams")
if str1==str1[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")