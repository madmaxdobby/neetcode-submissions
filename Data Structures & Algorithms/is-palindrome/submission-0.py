class Solution:
    def isPalindrome(self, s: str) -> bool:
        l="".join(ch for ch in s if ch.isalnum())
        m=l.strip(" ").lower()
        right=len(m)-1
        left=0
        n=""
        nrev=""
       
        while left<right:
            if m[left]==m[right]:
                n+=m[left]
                nrev+=m[right]
                left+=1
                right-=1
               
            else:
                return False
        
        if nrev==n:
            return True
        else:
            return False
