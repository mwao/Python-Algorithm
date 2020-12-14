import collections
from typing import Deque
   
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs:Deque=collections.deque()
        
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs)>1:
            #리스트의 pop(0)이 O(n) vs 데크의 popleft()는 O(1)
            #n번 반복 시 O(n^2) vs O(n) 
            if strs.popleft()!=strs.pop():
                return False
        return True 
