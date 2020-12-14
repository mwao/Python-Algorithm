class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=re.sub('[^a-z0-9]','',s)  #영숫자만 걸러내도록 처리 
        
        return s==s[::-1]   #[::-1]뒤집기 ,[::2] 2칸씩 이동 
