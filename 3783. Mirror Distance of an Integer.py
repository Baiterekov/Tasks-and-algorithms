# class Solution:
#     def mirrorDistance(n):
#         reverse = str(n)[::-1]  
#         return abs(n - int(reverse))
    
# print(Solution.mirrorDistance(12))


class Solution:
    def mirrorDistance(self, n: int) -> int:
        reverse = ""
        str_n = str(n)
        for i in range(0, len(str_n)):
            reverse = str_n[i] + reverse
        
        return abs(n - int(reverse))


# class Solution:
#     def mirrorDistance(n):
#         original = n
#         reverse = 0
#         while n:
#             reverse = reverse*10 + int(n%10)
#             n=n//10
#         return abs(original - reverse)
    
# print(Solution.mirrorDistance(25))
