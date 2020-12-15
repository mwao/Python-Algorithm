class Solution
    def reverseString(self, s List[str]) - None
# 01) 포인터를 활용한 스와프        
#         left, right=0,len(s)-1
#         while leftright
#             s[left],s[right]=s[right],s[left]
#             left+=1
#             right-=1

# 02) 리스트의 reverse() 함수 이용 
#         s.reverse()

# 03) 리스트의 슬라이싱 이용 (뒤집기 스킬 [-1])
#         s[]=s[-1]
        
