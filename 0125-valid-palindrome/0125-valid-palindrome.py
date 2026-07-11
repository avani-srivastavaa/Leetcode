class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=s.lower().strip('""')
        res=''
        for i in s1:
            if i.isalnum():
                res=res+i
        if res==res[::-1]:
            return True
        else:
            return False