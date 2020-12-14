class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs=[]
        for char in s:  # isalnum() 은 영문자,숫자 여부를 판별
            if char.isalnum():
                strs.append(char.lower())   # lower()로 소문자로
                
        while len(strs)>1:
            # pop()은 인덱스 지정 가능 / pop(0)은 0번째,맨앞의 값 / pop()은 맨 뒤의 값
            if strs.pop(0)!=strs.pop():
                return False
                
        return True
