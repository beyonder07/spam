def array(a, t):
    l, r = 0, len(a) - 1
    result = []
    c = 0
    while l < r:
        s = (a[l] + a[r])
        if s == t:
            result.append((a[l], a[r]))
            l += 1
            r -= 1   
            c += 1
        elif s < t:
            l += 1
        else:
            r -= 1
    print("Total count:", c)
    return result if result else "Not found"
a = list(map(int, input("Enter ").split()))
t = int(input("t = "))
print(array(a, t))
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = ''.join(c.lower() for c in s if c.isalnum())
#         left, right = 0, len(s) - 1  
#         while left < right:
#             if s[left] != s[right]: 
#                 return False
#             left += 1
#             right -= 1
        
#         return True
# sol = Solution()

# print(sol.isPalindrome("A man, a plan, a canal: Panama"))  
# print(sol.isPalindrome("racecar"))  
# print(sol.isPalindrome("hello"))  
# print(sol.isPalindrome("No 'x' in Nixon"))  
